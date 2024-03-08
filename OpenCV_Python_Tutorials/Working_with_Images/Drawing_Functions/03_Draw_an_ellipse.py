import cv2
import numpy as np

# read an input image
image = cv2.imread("puppy.jpg", 1)
print(image.shape)
# draw an ellipse
image = cv2.ellipse(image, (400,300), (100,50), 0, 0, 360, (0,0,255), 5)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Using thickness of -1 px and rotation of 30 degrees.
# read an input image
image = cv2.imread("puppy.jpg", 1)
print(image.shape)
# draw an ellipse
image = cv2.ellipse(image, (400,300), (100,50), 30, 0, 360, (0,0,255), 5)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()