import cv2
from matplotlib import pyplot as plt

import pywt
import pywt.data
import numpy as np

def show_gimg(gimg):
    plt.imshow(gimg,cmap='gray');
    plt.show()

img = cv2.imread("hermitage.jpg")
gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

wavelet = 'haar'
c = pywt.dwt2(gimg, wavelet)
cA, (cH, cV, cD)= c
#counts, edges = np.histogram(cA, bins=len(cA.flatten()))
h_vals, h_counts = np.unique(cA.flatten(), return_counts=True)
print(np.max(h_counts), np.max(h_vals))
show_gimg(cA)

for l in range(2):
    c = pywt.dwt2(c[0], wavelet)
    threshold = 70
    h1 = c[0].shape[0] # all the sets have the form of a square matrix
    for i in range(h1):
      c[0][i][np.abs(c[0][i])<threshold] = 0.0 # for cA
      #for j in range(len(c[1])):
         #c[1][j][i][np.abs(c[1][j][i])<threshold] = 0.0  # for cH,cV,cD
    print('The number of zeros =', sum(sum(c[0][m] == 0) for m in range(h1))) # (sum(sum(sum(c[1][m][n] == 0) for n in range(h1)) for m in range(len(c[1]))))
    show_gimg(c[0])


c_inverse1 = pywt.idwt2((c),wavelet)  # the coefficients are zeroed in the previous raw
titles1 = ['Original image', 'Restored image with new coefficients']
fig1 = plt.figure(figsize=(12, 6))
for i, a in enumerate([gimg,c_inverse1]):
  ax = fig1.add_subplot(1, 2, i + 1)
  ax.imshow(a, interpolation="nearest", cmap = 'gray')
  ax.set_title(titles1[i], fontsize=15)
fig1.tight_layout()
plt.show()