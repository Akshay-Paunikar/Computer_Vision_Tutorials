import numpy as np
import cv2

# read an input image
image = cv2.imread("puppy.jpg", 1)

# draw a rectangle
image = cv2.rectangle(image, (50, 50), (750,550), (0,0,255), 2)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Using thickness of -1 px to fill the rectangle by black color.
# read an input image
image = cv2.imread("puppy.jpg", 1)

# draw a rectangle
image = cv2.rectangle(image, (50, 50), (200,200), (0,0,0), -1)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()