import cv2
import numpy as np

img = cv2.imread("images/car.png")
# 将图像从 BGR 转换到 HSV 颜色空间
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 定义颜色范围，(蓝色区域)
lower = np.array([100, 100, 100])
upper = np.array([140, 255, 255])
# 使用 inRange 函数创建掩模
mask = cv2.inRange(hsv_image, lower, upper)
#二值化处理
ret, i_img = cv2.threshold(mask, 120, 255, cv2.THRESH_BINARY)
#获取图片的轮廓
myList, c = cv2.findContours(i_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

num = len(myList)
print(f"长度={num}")
for c in myList:
    x, y, w, h = cv2.boundingRect(c)
    print(x, y, w, h)
    #画个矩形
    if w > 100 and h > 45:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #车牌切割
        qie_img = img[y:y + h, x:x + w]
cv2.imshow("a", qie_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
