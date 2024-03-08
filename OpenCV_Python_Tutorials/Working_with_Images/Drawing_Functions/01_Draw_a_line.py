
import cv2

# read an input image
image = cv2.imread("puppy.jpg")

cv2.imshow("image", image)

# draw a line on above image
image_line = cv2.line(image, (0,0), (250,250), (0,255,0), 9)

cv2.imshow("image_line", image_line)

cv2.waitKey(0)
cv2.destroyAllWindows()
