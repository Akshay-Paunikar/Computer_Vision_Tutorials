# Shi-Tomasi method
import cv2
import numpy as np

# read the input image
image = cv2.imread("chess.png")

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# convert image to grayscale
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Shi-Tomasi corner detection function. We are detecting only 100 best corners here
# You can change the number to get desired result.
corners = cv2.goodFeaturesToTrack(gray_img, 100, 0.01, 10)

# convert corners values to integer. So that we will be able to draw circles on them
corners = np.int0(corners)

# draw red color circles on all corners
for i in corners:
    x, y = i.ravel()
    cv2.circle(image, (x, y), 3, (255, 0, 0), -1)

cv2.imshow("image", image)

# De-allocate any associated memory usage
cv2.waitKey(0)
cv2.destroyAllWindows()

# Harris Corner Detection method

# read the input image
image = cv2.imread('chess.png')

# convert the input image into
# grayscale color space
operatedImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# modify the data type
# setting to 32-bit floating point
operatedImage = np.float32(operatedImage)

# apply the cv2.cornerHarris method
# to detect the corners with appropriate
# values as input parameters
dest = cv2.cornerHarris(operatedImage, 2, 5, 0.07)

# Results are marked through the dilated corners
dest = cv2.dilate(dest, None)

# Reverting back to the original image,
# with optimal threshold value
image[dest > 0.01 * dest.max()] = [0, 0, 255]

# the window showing output image with corners
cv2.imshow('Image with Borders', image)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()