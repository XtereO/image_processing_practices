import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("task3.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.xlabel('Intensity $n$')
plt.ylabel('Amount')
img_new = img.copy()

print("rgb intensity", img[437][671])

line = lambda i:  (img[:, :, i] - np.min(img[:, :, i]))/(np.max(img[:, :, i]) - np.min(img[:, :, i]))*255
for i in range(3):
    img[:, :, i] = line(i)

print("rgb lined intensity", img[437][671])

cv2.imwrite("task3_output.jpg", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
