import numpy as np
import cv2

# read an input image
image = cv2.imread("puppy.jpg", 1)

# draw a text string
text = cv2.putText(image, "Cute Puppies", (75,75),cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 2)

cv2.imshow("text", text)
cv2.waitKey(0)
cv2.destroyAllWindows()