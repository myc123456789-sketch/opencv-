import cv2

img = cv2.imread('images/car.png')
# 图像色彩空间转换
# 图像默认BGR
# COLOR_BGR2HSV把图像转换成HSV图像
# 图像矩阵数据改变
gay_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('old',img)
cv2.imshow('new',gay_img)
cv2.waitKey(0)
cv2.destroyAllWindows()