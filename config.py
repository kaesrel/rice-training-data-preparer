

CHECKERBOARD = (5,7)

folder = {
    "input": "input",
    # "input": "bad_inputs",
    "input_by_cameras": "camera_inputs",
    "output": "test_output3",
    "output_by_undistort": "test_camera_output",
    "label_output": "test_label_output",
    "undistorted_label_output": "test_undistorted_label_output",
}

class_dict = {
    "rice_100": 0,
    "rice_5": 1,
    "rice_10": 2,
    "rice_15": 3,
}

random_seed = 1221
NUMBER_OF_IMAGES_TO_CALIBRATE = 40

CALIBRATE_CAMERA = False


epsilon = 0.1
max_definition = 11
tolerance = 0.5
DEBUG_WARPER = True
DEBUG_RECT = False
PRINT_MATRICES = False
PRINT_RECTANGLE_FINDER = False 

train = 0.6
valid = 0.2
test = 0.2


# class Config:

#     def __init__(self):
#         self.checkerboard = (5,7)  # h,w
#         self.folder = "./cammy"
#         self.out_folder = "./test_output"
#         self.epsilon = 0.1
#         self.max_definition = 11

# config = Config()
