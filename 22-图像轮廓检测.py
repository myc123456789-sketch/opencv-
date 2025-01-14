import cv2
import numpy as np

img = cv2.imread("images/car.png")
#把图像转换成HSV空间
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#获取蓝色所在的HSV范围
lower = np.array([100, 100, 50])
height = np.array([140, 255, 255])
#创建掩膜
#hsv_img 输入的图像是HSV图像
mask = cv2.inRange(hsv_img, lower, height)

#把图像转换成灰度图像
# #二值化处理
ret, t_img = cv2.threshold(mask, 20, 255, cv2.THRESH_BINARY)
# #检测轮廓
myList, c = cv2.findContours(t_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#
# #把图像转换成BGR图像
bgr_img = cv2.cvtColor(t_img, cv2.COLOR_GRAY2BGR)
#画出检测的轮廓的点
out_img = cv2.drawContours(bgr_img, myList, -1, (0, 255, 0), 1);
print(len(myList))
for c in myList:
    x, y, w, h = cv2.boundingRect(c)
    print(x, y, w, h)
    if w > 100 and h > 50:
        # 画出轮廓
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
        cai_img = img[y:y + h, x:w + x]
cv2.imshow("a", cai_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
