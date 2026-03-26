import cv2
import matplotlib.pyplot as plt

img = cv2.imread("task4.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

blured_img = cv2.GaussianBlur(img, (11, 3), 3)
cv2.imwrite("task4_out.jpg", cv2.cvtColor(img - blured_img, cv2.COLOR_RGB2BGR))
