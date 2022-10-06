import cv2
import sys
import numpy as np
from numba import jit
import argparse

# similarity threshold, 0 is perfect similarity,
thresh = 4444
path = ""
file = "3.mkv"
fps = 6
resolution = [1168, 657]

@jit(nopython=True)
def are_different(frame, next):
# check similarity between current frame and next one using MSE

    err = np.sum((frame - next)**2)/788544.0
    return (err > thresh)

# using two VideoCapture objects, we can choose between taking the next immediate frame or skipping
next_cap = cv2.VideoCapture(f"{path}{file}")
cap = cv2.VideoCapture(f"{path}{file}")

# throw away the first frame for next_cap
_, _ = next_cap.read()

skipped = 0
count = 0

ret, frame = cap.read()
next_ret, next_frame = next_cap.read()
frame = cv2.resize(frame, resolution)
next_frame = cv2.resize(next_frame, resolution)

while next_ret and ret:

    # check similarity between current frame and next one using MSE
    if (are_different(frame, next_frame)):

        # cv2.imshow("what", next_frame)
        # cv2.imshow("Big Diff", cv2.hconcat([frame,next_frame]))
        # cv2.waitKey(1)

        cv2.imwrite(f"{title}/{count}.PNG", frame)
        print(f"processed frame: {count}")

        skipped = 0
        count += 1

    elif (skipped == 6):

        # cv2.imshow("what", next_frame)
        # cv2.waitKey(1)

        cv2.imwrite(f"3/{count}.PNG", frame)
        print(f"processed frame: {count}")

        skipped = 0
        count += 1


    if not next_ret:
        print(f"Done cutting {title}")
        break

    # Step forward 1 frame
    ret, frame = cap.read()
    next_ret, next_frame = next_cap.read()
    frame = cv2.resize(frame, resolution)
    next_frame = cv2.resize(next_frame, resolution)

    skipped += 1


