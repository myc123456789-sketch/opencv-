import cv2

img = cv2.imread('images/car.png')
# 圆心坐标
center = (50, 50)
# 半径
radis = 50
# BGR颜色
color = (255, 0, 0)
# 线条宽度
w = 50
# 画圆
c_img = cv2.circle(img, center, radis, color)

cv2.imshow('img', c_img)
# waitKey(2000) 参数单位是毫秒
if cv2.waitKey(2000)==27:
    print('h')
# cv2.destroyAllWindows()

