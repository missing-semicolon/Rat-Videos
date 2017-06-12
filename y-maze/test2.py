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
    while(vid.isOpened()):
        counter += 1
        ret, frame = vid.read()
        if counter % 25 == 0:
            pass
            print("frame: {}, time: {}".format(counter, time.time() - start))

        frame = imutils.resize(frame, width=500)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if firstFrame is None:
            firstFrame = gray
        else:
            firstFrame = last_gray

        frameDelta = cv2.absdiff(firstFrame, gray)
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.ADAPTIVE_THRESH_MEAN_C)[1]
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, None)
        thresh = cv2.dilate(thresh, None, iterations=10)
        (_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # loop over contours
        for c in cnts:
            if cv2.contourArea(c) < 500:
                continue
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)

        cv2.imshow("thresh", thresh)
        cv2.imshow("input", frame)
        cv2.waitKey(1)
        last_gray = gray

    vid.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
