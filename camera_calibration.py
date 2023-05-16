import cv2
import numpy as np
import os, sys, random
import glob
import config
from resizer import resizer


criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Creating vector to store vectors of 3D points for each checkerboard image
objpoints = dict()
# Creating vector to store vectors of 2D points for each checkerboard image
imgpoints = dict()

not_found_corner = dict()

# for cam in os.listdir(f"{config.folder['input']}"):
#     objpoints[cam] = []
#     imgpoints[cam] = []
#     not_found_corner[cam] = []


CHECKERBOARD = config.CHECKERBOARD

objp = np.zeros((1, CHECKERBOARD[0]*CHECKERBOARD[1], 3), np.float32)
objp[0,:,:2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)

# print(len(imgs_to_calibrate))
# print(imgs_to_calibrate)

for cam in os.listdir(f"{config.folder['input']}"):
    print(cam)
    objpoints[cam] = []
    imgpoints[cam] = []
    not_found_corner[cam] = []

    images = glob.glob(f"{config.folder['input']}/{cam}/**/*.jpg")



    random.seed(config.random_seed)
    random.shuffle(images, random.random)
    end_slice = min(config.NUMBER_OF_IMAGES_TO_CALIBRATE, len(images))
    imgs_to_calibrate = images[:end_slice] # get random images to get calibration parameters

    for fname in imgs_to_calibrate:
        img = cv2.imread(fname)
        img = resizer.resize(img)
        cname = fname.split('/')[-2]

        # print(fname.split('/'))

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, cv2.CALIB_CB_ADAPTIVE_THRESH+
            cv2.CALIB_CB_FAST_CHECK+cv2.CALIB_CB_NORMALIZE_IMAGE)

        # if cam == "camera1":
        #     print(cname)


        if ret == True:

            objpoints[cam].append(objp)
            # refining pixel coordinates for given 2d points.

            corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
            
            imgpoints[cam].append(corners2)
            # Draw and display the corners
            my_img = img.copy()
            my_img = cv2.drawChessboardCorners(my_img, CHECKERBOARD, corners2,ret)
            cv2.imwrite(f"chessboard_demo/{fname.split('/')[-1]}", my_img)
        else:
            not_found_corner[cam].append(fname)
        



for cam in os.listdir(f"{config.folder['input']}"):
    imgpoints_array = np.array(imgpoints[cam])
    objpoints_array = np.array(objpoints[cam])
    # np.savetxt("imgpoints.txt", imgpoints_array)
    # np.savetxt("objpoints.txt", objpoints_array)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints[cam], imgpoints[cam], gray.shape[::-1],None,None)

    with open(f"{config.folder['input']}/{cam}/camera_matrix.npy", "wb") as f:
        np.save(f, mtx)
        np.save(f, dist)
   

    # with open(f"{config.folder['input']}/{cam}/camera_matrix.npy", "rb") as f:
    #     my_mtx = np.load(f)
    #     my_dist = np.load(f)



    # print("Expected:")
    # print("Camera matrix : \n")
    # print(mtx)
    # print("dist : \n")
    # print(dist)

    # print("Actual:")
    # print("Camera matrix : \n")
    # print(my_mtx)     
    # print("dist : \n")
    # print(my_dist)

    # print(f"mtx == my_mtx is {mtx == my_mtx}")
    # print(f"dist == my_dist is {dist == my_dist}")



    # print("rvecs : \n")
    # print(rvecs)
    # print("tvecs : \n")
    # print(tvecs)




