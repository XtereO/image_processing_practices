import numpy as np
import cv2
from matplotlib import pyplot as plt


def show_gray_img(img):
    plt.imshow(img, cmap="gray")
    plt.show()


img = cv2.imread("hummingbird.jpg")
gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rows, cols = gimg.shape
print("img sizes", rows, cols)

f = np.fft.fft2(gimg)
print("fourier pixel at (563,563)", f[563][563])

fshift = np.fft.fftshift(f)
m_f = np.abs(fshift)
print("fourier magnitude min&max", np.min(m_f), np.max(m_f))

lm_f = np.log(1+m_f)
show_gray_img(lm_f)
print("the difference between max&min lmf", np.max(lm_f)-np.min(lm_f))

shift_index = 40
fshift[rows//2 - shift_index: rows//2 + shift_index,
       cols//2-shift_index: cols//2 + shift_index] = 0
lm_f = np.log(1+np.abs(fshift))
show_gray_img(lm_f)

f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
show_gray_img(img_back)
print("inverse fourier pixel at (624,399)", np.abs(img_back[624][399]))
