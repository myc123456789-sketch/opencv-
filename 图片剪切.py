import cv2
import numpy as np

img = cv2.imread('images/car.png')
(h, w) = img.shape[:2]
# 定义图片剪切参数
sx = 0.2
sy = 0.5
# 定义矩阵
m = np.float32([[1, sx, 0], [sy, 1, 0]])

i_img = cv2.warpAffine(img, m, (h, w))
cv2.imshow('image', i_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
