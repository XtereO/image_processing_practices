import cv2
from matplotlib import pyplot as plt

import pywt
import pywt.data
import numpy as np

def show_gimg(gimg):
    plt.imshow(gimg,cmap='gray');
    plt.show()

img = cv2.imread("spb_m.jpg")
gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

wavelet = 'haar'
c = pywt.dwt2(gimg, wavelet)
cA, (cH, cV, cD)= c
#counts, edges = np.histogram(cA, bins=len(cA.flatten()))
h_vals, h_counts = np.unique(cA.flatten(), return_counts=True)
print(np.max(h_counts), np.max(h_vals))


if (False):
    show_gimg(cA)
    show_gimg(cH)
    show_gimg(cV)
    show_gimg(cD)