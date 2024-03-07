# import libraries
import cv2
import numpy as np

# Read the image in grayscale
image = cv2.imread("blobs.png", 0)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# set filtering parameters using cv2.SimpleBlobDetector
params = cv2.SimpleBlobDetector_Params()

# set area filtering parameters
params.filterByCircularity = True
params.minCircularity = 0.9

# set convexity filtering parameters
params.filterByConvexity = True
params.minConvexity = 0.2

# set inertia filtering parameters
params.filterByInertia = True
params.minInertiaRatio = 0.01

# create a detector with parameters
detector = cv2.SimpleBlobDetector_create(params)

# detect blobs
keypoints = detector.detect(image)

# Draw blobs on our image as red circles
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255),
                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = "Number of Circular Blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 550),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)

# Show blobs
cv2.imshow("Filtering Circular Blobs Only", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()

