import cv2

img = cv2.imread('images/car.png')
# 翻转,0垂直翻转，1水平翻转（镜像），-1，水平+垂直翻转。
f_img = cv2.flip(img, -1)

cv2.imshow('new', f_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
