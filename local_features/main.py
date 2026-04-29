import cv2 
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
from PIL import Image

mpl.rcParams['figure.dpi'] = 200

img = cv2.imread("tokyo.jpg")
sub_img = img[353:503, 550:695]
print(sub_img.shape)

gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sub_gimg = cv2.cvtColor(sub_img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(gimg, None)
kp2, des2 = sift.detectAndCompute(sub_gimg, None)

bf = cv2.BFMatcher(cv2.NORM_L1,crossCheck=True)
#crossCheck=false - one-to-many matches, crossCheck=true - one-to-one matches
matches = bf.match(des1,des2)

matches = sorted(matches, key = lambda x:x.distance)
print('Matches rate ', len(matches))
print('Distance ', matches[0].distance, 'Index 1 ', matches[0].trainIdx, 'Index 2 ', matches[0].queryIdx)
print("coordinates", kp1[matches[0].queryIdx].pt, kp2[matches[0].trainIdx].pt)
print("bgr value", img[451][561], sub_img[98][11])
#new1 = np.float32([kp1[m.queryIdx].pt for m in matches]) # the coordinates of the keypoint of the 1st image
#new2 = np.float32([kp2[m.trainIdx].pt for m in matches]) 

matching_result = cv2.drawMatches(gimg, kp1, sub_gimg, kp2, matches[:99], None,[255,0,0], flags=2)

mpl.rcParams['figure.dpi'] = 200
plt.axis('off')
plt.imshow(cv2.cvtColor(matching_result, cv2.COLOR_BGR2RGB))
plt.show()