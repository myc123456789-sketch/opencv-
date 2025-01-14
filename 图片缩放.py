import cv2
import numpy as np

img = cv2.imread('images/car.png')
(h, w) = img.shape[:2]
# 定义缩放的参数,参数大于1放大，小于1缩小
ww = 0.5
hh = 0.5

m = np.float32([[ww, 0, 0], [0, hh, 0]])
# 仿射变换
t_img = cv2.warpAffine(img, m, (int(w * ww), int(h * hh)))

cv2.imshow('image', t_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
