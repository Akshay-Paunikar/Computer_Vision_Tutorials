import numpy as np
import cv2

# read an input image
image = cv2.imread("puppy.jpg", 1)

# draw an arrow segment
image = cv2.arrowedLine(image, (0,0), (300,300), (0,255,0), 9)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()