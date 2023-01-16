import cv2
import numpy as np
import glob, os, sys
import config
import preprocess_state as state
from resizer import resizer
from warper import warper
from masker import masker
from rectangle_finder import rectangle_finder
from annotator import annotator


# images = glob.glob(f"{config.folder['input']}/*.jpg")


input_folder = config.folder['input']

state.mask_errors = []
state.cannot_draw = []
state.not_squares = []


# images = glob.glob(f"{config.folder['input']}/**/*.jpg")
# print(len(images))
# print(images)

cameras = os.listdir(f"{config.folder['input']}")
output_folder = config.folder['output']
state.label_output_folder = config.folder['label_output']

if not os.path.exists(f"{output_folder}"):
    os.makedirs(f"{output_folder}")

if not os.path.exists(f"{state.label_output_folder}"):
    os.makedirs(f"{state.label_output_folder}")


i=1
for cam in cameras:

    state.is_calibrated = False

    mtx = None
    dist = None
    if config.CALIBRATE_CAMERA:
        try:
            with open(f"{config.folder['input']}/{cam}/camera_matrix.npy", "rb") as f:
                mtx = np.load(f)
                dist = np.load(f)
        except (OSError, FileNotFoundError) as error:
            print("WHAT THE HECK?!")
            pass

    images = glob.glob(f"{input_folder}/{cam}/**/*.jpg")


    print(len(images))
    print(images)

    for fname in images:
        state.fname = fname
        state.cname = fname.split('/')[-2]
        print(fname.split('/'))
        img = cv2.imread(fname)
        img = resizer.resize(img)
        h,w = img.shape[:2]

        if (not mtx is None) and (not dist is None):
            newcameramtx, dist_roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
            img = cv2.undistort(img, mtx, dist, None, newcameramtx)  # undistorted image
            state.is_calibrated = True

        is_warped, warped = warper.warp(img)
        roi = masker.get_roi(warped)

        try:
            mask = masker.mask(roi)
        except cv2.error:
            state.mask_errors.append(state.fname)
            i+=1
            continue

        ret = rectangle_finder.find_rectangle(mask, warped)


        if ret:
            if not os.path.exists(f"{output_folder}/{state.cname}"):
                os.makedirs(f"{output_folder}/{state.cname}")
            cv2.imwrite(f"{output_folder}/{state.cname}/{fname.split('/')[-1]}", warped)
            annotator.annotate(warped)
        else:
            state.cannot_draw.append(state.fname)

        i+=1

# sys.exit

print("====================================================")
print("MASK ERRORS:")
print(len(state.mask_errors))
print(state.mask_errors)
print("====================================================")
print("CANNOT DRAW:")
print(len(state.cannot_draw))
print(state.cannot_draw)
print("====================================================")
print("NOT SQUARES:")
print(len(state.not_squares))
print(state.not_squares)


# print("###################BEGIN ANNOTATION###################")
# images = glob.glob(f"{output_folder}/**/*.jpg")
# for fname in images:
#     annotator.annotate(fname)

print("###################GENERATE YOLO PARAMS###################")
annotator.generate_yolo_param_files()