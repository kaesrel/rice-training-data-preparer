import cv2
import numpy as np
import config
import preprocess_state as state


class Warper:
    def __init__(self):
        pass

    def find_corners(self, img, criteria=None):
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(gray, config.CHECKERBOARD, cv2.CALIB_CB_ADAPTIVE_THRESH+
    	    cv2.CALIB_CB_FAST_CHECK+cv2.CALIB_CB_NORMALIZE_IMAGE)

        if ret == True:
            if criteria == None:
                criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
            # refining pixel coordinates for given 2d points.
            corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
            if config.DEBUG_WARPER:
                a = img.copy()
                a = cv2.drawChessboardCorners(a, config.CHECKERBOARD, corners2,ret)
                cv2.imwrite("outty/chess_draw.jpg",a)

            return True, corners2
        
        return False, None
   


    def warp(self, img):
        corner_found, corners = self.find_corners(img)

        if not corner_found:
            return False, img

        corner_size = config.CHECKERBOARD

        nh, nw = corner_size
        nh -= 1
        nw -= 1
        h,w = img.shape[:2]

        smat = np.float32([
            corners[0][0],
            corners[corner_size[0]-1][0],
            corners[len(corners)-corner_size[0]][0],
            corners[len(corners)-1][0]
        ])
        
        # smat[0] topright: b
        # smat[1] botright: d
        # smat[2] topleft: a
        # smat[3] botleft: c

        # centers
        xc = sum([p[0] for p in smat])/len(smat)
        yc = sum([p[1] for p in smat])/len(smat)

        # deltas
        dx = ((-smat[2][0] + smat[0][0] - smat[3][0] + smat[1][0])/2) / nw  # Ratio x
        dy = ((-smat[2][1] + smat[3][1] - smat[0][1] + smat[1][1])/2) / nh  # Ratio y

        dt = (dx + dy) / 2  # Ratio average
        dcx = (dt*nw) / 2  # Center distance
        dcy = (dt*nh) / 2

        dmat = np.float32([
            [xc + dcx, yc - dcy], # b
            [xc + dcx, yc + dcy], # d
            [xc - dcx, yc - dcy], # a
            [xc - dcx, yc + dcy], # c
        ])

        if config.PRINT_MATRICES:
            print("source matrix:")
            print(smat)
            print("dest matrix:")
            print(dmat)

        M = cv2.getPerspectiveTransform(smat, dmat)

        tol = config.tolerance

        off_x1 = max(corner_size)+1 + 2 + 1 + tol
        off_y1 = 1 + tol
        off_x2 = 2
        off_y2 = max(corner_size) + tol

        x_1 = int(dmat[2][0] - dt*off_x1)
        y_1 = int(dmat[2][1] - dt*off_y1)
        x_2 = int(dmat[2][0] - dt*off_x2)
        y_2 = int(dmat[2][1] + dt*off_y2)

        state.dt = dt
        state.rpts = np.array([np.array([x_1,y_1]), np.array([x_2,y_2])])
        state.offset = np.array([x_1, y_1])

        return True, cv2.warpPerspective(img, M, (w,h), flags=cv2.INTER_LINEAR)






warper = Warper()