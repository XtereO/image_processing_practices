import cv2

img = cv2.imread("task2.jpg")

cropped_img = img[876:1555, 1594:2153]
cv2.imshow("cropped img", cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
