import os
import numpy as np
import time
import imutils
import cv2


def main():
    vid = cv2.VideoCapture('WIN_20161117_14_19_14_Pro.mp4')
    start = time.time()
    firstFrame = None

    counter = 0

    fgbg = cv2.createBackgroundSubtractorMOG2()
    while(vid.isOpened()):
        counter += 1
        ret, frame = vid.read()
        if counter % 25 == 0:
            pass
            print("frame: {}, time: {}".format(counter, time.time() - start))

        frame = imutils.resize(frame, width=500)

        fgmask = fgbg.apply(frame)
        fgmask = cv2.GaussianBlur(fgmask, (21, 21), 0)

        (_, cnts, _) = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in cnts:
            if cv2.contourArea(c) < 500:
                continue
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)        

        cv2.imshow("thresh", fgmask)
        cv2.imshow("input", frame)
        cv2.waitKey(1)
        # last_gray = gray

    vid.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
