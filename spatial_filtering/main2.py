import cv2
import matplotlib.pyplot as plt

img = cv2.imread("task2.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

red_hist = plt.hist(img[:, :, 0].ravel(), bins = 256, color = 'Red', alpha = 0.5, density=True)
green_hist = plt.hist(img[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5, density=True)
blue_hist = plt.hist(img[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5, density=True)
plt.legend(['Red channel (R)', 'Green channel (G)', 'Blue channel (B)'])
plt.xlabel('Intensity $n$')
plt.ylabel('Number')
plt.show()

print("max density", round(max([*blue_hist[0], *green_hist[0], *red_hist[0]])/sum(blue_hist[0]), 5))