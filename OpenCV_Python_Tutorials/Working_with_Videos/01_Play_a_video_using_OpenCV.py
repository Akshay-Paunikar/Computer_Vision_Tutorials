# import libraries
import numpy as np
import cv2

# first let's capture the live video
cap = cv2.VideoCapture(0)

# check if camera is opened or not
if (cap.isOpened()==False):
    print("Error in opening the camera")

# read until video is completed
while (cap.isOpened()):
    ret, frame = cap.read() # capture frame by frame
    if ret == True:
        cv2.imshow("frame", frame) # display the resulting frame
        # press "q" on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # break the loop
    else:
        break

# after everything is done release the video
cap.release()

# close all the frames
cv2.destroyAllWindows()

# create a video capture object and read the input file