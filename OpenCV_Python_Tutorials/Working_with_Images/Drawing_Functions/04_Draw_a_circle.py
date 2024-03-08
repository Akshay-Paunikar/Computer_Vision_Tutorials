import numpy as np
import cv2

# read an input image
image = cv2.imread("puppy.jpg", 1)

# draw a circle
image = cv2.circle(image, (400, 300), 100, (255,0,0), 2)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Using thickness of -1 px to fill the circle with red color.
# read an input image
image = cv2.imread("puppy.jpg", 1)

# draw a circle
image = cv2.circle(image, (400, 300), 100, (255,0,0), -1)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()