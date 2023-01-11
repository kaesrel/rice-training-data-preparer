import cv2
import numpy as np
import config
import preprocess_state as state
from data_splitter import datasplitter


class Annotator:
    def __init__(self) -> None:
        pass

    def convert_coordinate(self, w, h):
        # state.rect_coordinates = np.array([pt1,pt2])
        x1 = state.rect_coordinates[0][0]
        y1 = state.rect_coordinates[0][1]
        x2 = state.rect_coordinates[1][0]
        y2 = state.rect_coordinates[1][1]
        
        x_center = int ((x2 - x1) / 2) / w
        y_center = int ((y2 - y1) / 2) / h
 
        # box_center = np.array([x_centre_norm, y_centre_norm])
        
        box_width = (x2  - x1) / w
        box_height = (x2  - x1) / h

        return x_center, y_center, box_width, box_height


    def annotate(self, fname):
        img = cv2.imread(fname)
        imgname = fname.split('/')[-1]
        class_num = config.class_dict[fname.split('/')[-2]]
        # class_num = 0
        img_id = imgname.split('.')[0]
        h,w = img.shape[:2]
        xc, yc, bw, bh = self.convert_coordinate(w,h)

        out_file = open(f"{state.label_output_folder}/{img_id}.txt", 'w')
        out_file.write(f"{class_num} {xc} {yc} {bw} {bh}\n")
        cv2.imwrite(f"{state.label_output_folder}/{img_id}.jpg", img)


    def generate_yolo_param_files(self):
        obj_names = open(f"obj.names", "w")
        object_data = open(f"object.data", "w")
        train = open(f"train.txt", "w")
        valid = open(f"validation.txt", "w")
        test = open(f"test.txt", "w")

        sorted_class = sorted(config.class_dict.items(), key=lambda x:x[1])

        for c in sorted_class:
            obj_names.write(f"{c[0]}\n")
            datasplitter.split_data(c[0])

            for train_file in state.train_files:
                train.write(f"{state.label_output_folder}/{train_file}\n")
            for valid_file in state.valid_files:
                valid.write(f"{state.label_output_folder}/{valid_file}\n")
            for test_file in state.test_files:
                test.write(f"{state.label_output_folder}/{test_file}\n")
            
        object_data.write(f"classes = {len(config.class_dict)}\n")
        object_data.write(f"train = train.txt\n")
        object_data.write(f"valid = validation.txt\n")
        object_data.write(f"test = test.txt\n")
        object_data.write(f"names = obj.names\n")

        # print(sorted_class)








# def save_annotations(img, boxes):
#     img_height = img.shape[0]
#     img_width = img.shape[1]
#     with open('image.txt', 'w') as f:
#         for box in boxes:
#             x1, y1 = box[0], box[1]
#             x2, y2 = box[2], box[3]
             
#             if x1 > x2:
#                 x1, x2 = x2, x1
#             if y1 > y2:
#                 y1, y2 = y2, y1
                 
#             width = x2 - x1
#             height = y2 - y1
#             x_centre, y_centre = int(width/2), int(height/2)
 
#             norm_xc = x_centre/img_width
#             norm_yc = y_centre/img_height
#             norm_width = width/img_width
#             norm_height = height/img_height
 
#             yolo_annotations = ['0', ' ' + str(norm_xc), 
#                                 ' ' + str(norm_yc), 
#                                 ' ' + str(norm_width), 
#                                 ' ' + str(norm_height), '\n']
             
#             f.writelines(yolo_annotations)


annotator = Annotator()