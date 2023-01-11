import cv2
import numpy as np
import preprocess_state as state


class Masker:
    def __init__(self) -> None:
        pass

    def mask(self, img):
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


        return cv2.Laplacian(gray, cv2.CV_8UC1, ksize=3)
        # return cv2.Canny(gray,100,200)

        # # cv2.imwrite("outty/edge.jpg", edges)


        # # ret,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        # # thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
        # #             cv2.THRESH_BINARY,11,2)

        # thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
        #             cv2.THRESH_BINARY,11,2)

        # # blur = cv2.GaussianBlur(gray,(5,5),0)
        # # ret,thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        # img = cv2.inRange(thresh, 0, 90)

        
        # # img = (255-thresh)

        # # TODO: perform dilation/erosion/etc.
        # # kernel = np.ones((5, 5), np.uint8)
        # # img = cv2.dilate(img, kernel, iterations=1)
        # # img = cv2.erode(img, kernel, iterations=1)


    def get_roi(self, img):
        rp = state.rpts
        return img[rp[0][1]:rp[1][1], rp[0][0]:rp[1][0]]  # y1:y2, x1:x2


        
masker = Masker()
