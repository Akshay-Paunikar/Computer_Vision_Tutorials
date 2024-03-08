import numpy as np
import cv2

# read an input image
image = cv2.imread("puppy.jpg", 1)

cv2.imshow("image", image)

# draw a line on above image
image_line = cv2.line(image, (0,0), (250,250), (0,255,0), 9)

cv2.imshow("image_line", image_line)

cv2.waitKey(0)
cv2.destroyAllWindows()

# draw a line on black screen using numpy library
# create a black screen using numpy
image = np.zeros((512, 512, 3), dtype='uint8')

# draw a line
image_black = cv2.line(image, (0,0), (250,250), (255, 255, 255), 9)

cv2.imshow("image_black", image_black)

cv2.waitKey(0)
cv2.destroyAllWindows()