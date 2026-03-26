import cv2

img = cv2.imread("task5.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_blured = cv2.medianBlur(img, 9)
cv2.imwrite("task5_out.jpg", img_blured)
