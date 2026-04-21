import numpy as np
import cv2
from matplotlib import pyplot as plt


def show_gray_img(img):
    plt.imshow(img, cmap="gray")
    plt.show()


img = cv2.imread("waterscape.jpg")
gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
limg = cv2.Laplacian(img, -1)
show_gray_img(limg)
print("[Laplacian] sum of all intensities", np.sum(limg))

cimg = cv2.Canny(img, 100, 200)
show_gray_img(cimg)
print("[Canny] sum of all intensities", np.sum(cimg))