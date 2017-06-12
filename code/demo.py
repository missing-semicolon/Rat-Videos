import os
import time
import numpy as np
import cv2


def main():
    data_dir = '../y-maze/'
    for y_vid in os.listdir(data_dir):
        vid = cv2.VideoCapture(os.path.join(data_dir, y_vid))
        start = time.time()

        counter = 0
        while(vid.isOpened()):
            counter += 1
            ret, frame = vid.read()
            if counter % 25 == 0:
                print("time: {}".format(time.time() - start))
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # cv2.imshow("input", frame)
            # cv2.waitKey(120)

        # vid.release()
        # cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
