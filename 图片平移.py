import cv2
import numpy as np

img = cv2.imread('images/car.png')
(h, w) = img.shape[:2]
# 定义水平和垂直移动的距离
ty = 50
tx = 100
# 创建平移矩阵
t_img = np.float32([[1, 0, tx], [0, 1, ty]])
# t_img = cv2.getRotationMatrix2D((tx, ty), -1, 1)
w_img = cv2.warpAffine(img, t_img, (w, h))

cv2.imshow('image', w_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
