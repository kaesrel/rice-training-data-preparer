import cv2
import numpy as np
import math
import config

class Resizer:
    def __init__(self):
        pass

    def resize(self, img):
        h,w = img.shape[:2]

        max_size = config.max_definition

        if max(w,h) <= 2**max_size:
            return img
        else:
            power = math.ceil(math.log2(max(w,h))) - max_size
            # print(power)
            w = w // (2**power)
            h = h // (2**power)
            print(f"width={w}, height={h}")
            return cv2.resize(img, (w,h), interpolation=cv2.INTER_LINEAR)


resizer = Resizer()