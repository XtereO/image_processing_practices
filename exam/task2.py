import math
import numpy as np

from matplotlib import pyplot as plt
import cv2
import pywt
import pywt.data

img = cv2.imread("tim.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
h, w, _p = img.shape
nw = 4200
ratio = h/w
nh = math.floor(nw*ratio)
print("height and ratio", nh, w/h)

cimg = cv2.resize(img, (nw, nh), interpolation=cv2.INTER_AREA)
print(cimg.shape)

blue = np.histogram(cimg[:,:,0], bins=256, density=True)
green = np.histogram(cimg[:,:,1], bins=256, density=True)
red = np.histogram(cimg[:,:,2], bins=256, density=True)

print(np.max(blue[0]), np.max(red[0]), np.max(green[0]))

line = lambda m: ((m-np.min(m))/(np.max(m)-np.min(m)))*255
limg = cimg.copy()
for i in range(3):
    limg[:, :, i] = line(limg[:, :, i])

print("stretched pixel", limg[1514][2064])

plt.imshow(limg)
plt.show()

gimg = cv2.cvtColor(limg, cv2.COLOR_RGB2GRAY)
wavelet = "haar"
cA, (cH, cV, cD) = pywt.dwt2(gimg, wavelet)
print(cA.shape)
cA2, _c2 = pywt.dwt2(cA, wavelet)
T = 110

#cA1, (cH1, cV1, cD1) = pywt.dwt2(cA,wavelet)

r, c = cA2.shape
zeros = 0
for i in range(r):
    for j in range(c):
        if(abs(cA2[i][j]) < T): 
            cA2[i][j] = 0
            zeros+=1
        #zeros+= 1 if abs(cA2[i][j][0])<T else 0
print(zeros)

print('The number of zeros in the set cA =',sum(sum(cA2[m] == 0) for m in range(len(cA2))))

plt.imshow(cA2,cmap="gray")
plt.show()