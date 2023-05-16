

CHECKERBOARD = (5,7)

folder = {
    # "input": "input",
    # "input": "bad_inputs",
    "input": "camera_inputs",
    # "output": "test_output",
    "output": "mixed_dense_sparse",
    # "output": "compare",
    "label_output": "mixed_dense_sparse_label",
    # "label_output": "for_show_label",
    "undistorted_label_output": "test_undistorted_label_output",
}

class_dict = {
    "rice_100": 0,
    "rice_5": 1,
    "rice_10": 2,
    "rice_15": 3,
}

# class_dict = {
#     "rice_100_dense": 0,
#     "rice_5_dense": 1,
#     "rice_10_dense": 2,
#     "rice_15_dense": 3,
#     "rice_100_sparse": 4,
#     "rice_5_sparse": 5,
#     "rice_10_sparse": 6,
#     "rice_15_sparse": 7,
# }


random_seed = 1221
NUMBER_OF_IMAGES_TO_CALIBRATE = 40

CALIBRATE_CAMERA = True


epsilon = 0.1
max_definition = 11
tolerance = 0.5
tight_factor = 0.04
DEBUG_WARPER = False
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
