import cv2
import numpy as np
import config
import preprocess_state as state

class RectangleFinder:
    def __init__(self) -> None:
        pass

    def find_rectangle(self, roi, img):
        contours, hierarchy = cv2.findContours(roi, cv2.RETR_EXTERNAL, 2)

        # state.rect_coordinates = np.array([])

        if config.PRINT_RECTANGLE_FINDER:
            print("Number of contours detected:", len(contours))
            print(hierarchy)

        eps1 = config.epsilon
        eps2 = config.epsilon

        # print(state.fname)
        for cnt in contours:
            x1,y1 = cnt[0][0]
            approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
            if len(approx) == 4:
                if config.PRINT_RECTANGLE_FINDER:
                    print(approx)
                x, y, w, h = cv2.boundingRect(cnt)
                square_ratio = float(w)/h
                square_size = max(config.CHECKERBOARD) + 1
                len_ratio = (w+h)/(state.dt * square_size * 2)
                if abs(square_ratio - 1.0) <= eps1 and abs(len_ratio - 1.0) <= eps2:
                    dw = round(w*config.tight_factor/2)
                    dh = round(h*config.tight_factor/2)
                    # dw = 16
                    # dh = 16
                    pt1 = (x, y) + state.offset + (dw, dh)
                    pt2 = (x+w, y+h) + state.offset - (dw, dh)
                    print(f"Points are: {pt1} {pt2}")
                    print(f"dw dh are: {dw} {dh}")
                    if config.DEBUG_RECT:
                        cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)
                        # cv2.putText(img, 'Square', (x1,y1) + state.offset, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
                        cv2.putText(img, 'rice_100', (x,y) + state.offset, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
                    state.rect_coordinates = np.array([pt1,pt2])

                    return True
                # else:
                #     state.not_squares.append(state.fname)
                #     cv2.putText(roi, 'Rectangle', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                #     rec = cv2.drawContours(img, [cnt], -1, (0,255,0), 1)
                    # return False, rec
        return False

rectangle_finder = RectangleFinder()