import cv2
import numpy as np

img = cv2.imread('images/ceshi01.jpeg')
# 定义膨胀参数
k = np.ones((5, 5), np.uint8)
# 膨胀次数
num = 2
# 膨胀操作
e_img = cv2.dilate(img, k, iterations=num)
cv2.imshow('img', img)
cv2.imshow('E', e_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
