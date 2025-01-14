import cv2

img = cv2.imread('images/car.png')
# 直线起始
start = (100, 100)
# 截止坐标
end = (200, 200)
# color
color = (0, 255, 0)
# 宽度
w = 2
l_img = cv2.line(img, start, end, color, w)
cv2.imshow('img', l_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
