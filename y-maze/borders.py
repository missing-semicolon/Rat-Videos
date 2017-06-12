import os
import numpy as np
import time
import imutils
import cv2


def area(box):
    a = box[0]
    b = box[1]
    c = box[2]

    len_ab = np.linalg.norm(a - b)
    len_bc = np.linalg.norm(b - c)
    return len_ab * len_bc


def main():
    vid = cv2.VideoCapture('WIN_20161117_14_19_14_Pro.mp4')
    start = time.time()
    firstFrame = None

    counter = 0

    while(vid.isOpened()):
        counter += 1
        ret, frame = vid.read()
        if counter % 25 == 0:
            pass
            print("frame: {}, time: {}".format(counter, time.time() - start))

        frame = imutils.resize(frame, width=500)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(frame, 100, 200)
        edges = cv2.GaussianBlur(edges, (21, 21), 0)

        _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)



        cv2.imshow("thresh", edges)
        cv2.imshow("thresh", thresh)
        cv2.imshow("input", frame)
        cv2.waitKey(1)
        # last_gray = gray

    vid.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
