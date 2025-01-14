import cv2

img = cv2.imread('images/car.png')
# 获取图片像素
(h, w) = img.shape[:2]
# 旋转坐标
center = (100, 100)
# 旋转角度
du = 30
# 获取图片矩阵
m = cv2.getRotationMatrix2D(center, du, 1)
w_img = cv2.warpAffine(img, m, (w, h))
cv2.imshow('image', w_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
