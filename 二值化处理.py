import cv2

img = cv2.imread('images/car.png')
# 把图像灰度处理
g_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 二值化处理
# rs,实际应用阈值，t_img,转换后的图像
rs,t_img=cv2.threshold(g_img,100,255,cv2.THRESH_BINARY)
cv2.imshow('a',t_img)
cv2.waitKey(0)
cv2.destroyAllWindows()