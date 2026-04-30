import math
import numpy as np

import cv2
import pywt


img = cv2.imread("fr.jpg")
gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h, w = gimg.shape
ratio = h/w
nw = 2661
nh = math.floor(nw*ratio)
print("ratio w/h", w/h, nh)
cimg = cv2.resize(img, (nw, nh), interpolation=cv2.INTER_AREA)

blue = np.histogram(cimg[:, :, 0].ravel(), 256, density=True)
green = np.histogram(cimg[:, :, 1].ravel(), 256, density=True)
red = np.histogram(cimg[:, :, 2].ravel(), 256, density=True)

print(max(np.max(blue[0]), np.max(green[0]), np.max(red[0])))

line = lambda m: ((m-np.min(m))/(np.max(m)-np.min(m)))*255
limg = cimg.copy()
for i in range(3): 
    limg[:, :, i] = line(limg[:, :, i])

print("stretched pixel:", limg[914][1291])
print(np.min(limg[:, :, 0]), np.min(limg[:, :, 1]), np.min(limg[:, :, 2]))

wavelet = "Haar"
cA, m = pywt.dwt2(limg, wavelet)
cA, m = pywt.dwt2(cA, wavelet)
T = 40
r, c, _d = cA.shape
zeros = 0
for i in range(r):
    for j in range(c):
        zeros += 1 if (cA[i][j][0] < T) else 0
print(zeros, np.min(cA[:, :, 0]))
