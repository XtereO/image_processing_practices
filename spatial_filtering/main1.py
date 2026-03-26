import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("task1.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img_ravel = gray_img.ravel()

gray_hist = plt.hist(gray_img_ravel, bins = 256)
print(gray_hist)
plt.xlabel('Intensity $n$')
plt.ylabel('Number $h(n)$')
plt.show()

max_gray = max(gray_hist[0])
max_gray_index = gray_hist[1][list(gray_hist[0]).index(max_gray)]

print(max_gray, max_gray_index)
