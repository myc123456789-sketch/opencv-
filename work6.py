import cv2
import numpy as np
from myocr.MyUtile1 import demo01

img = cv2.imread('images/wenzi01.jpeg')
gay_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
k = np.ones((9, 9), np.uint8)
close_img = cv2.morphologyEx(gay_img, cv2.MORPH_BLACKHAT, k)
k1 = (19, 19)
d = 2
gs_img = cv2.GaussianBlur(close_img, k1, d)
c_img = cv2.Canny(gs_img, 180, 200)
open_img = cv2.dilate(c_img, np.ones((19, 19)), iterations=1)
contours, hierarchy = cv2.findContours(open_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
num = len(contours)
print(f"长度={num}")
qie_img = 0
qie1_img = 0
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    print(x, y, w, h)
    if w == 355:
        c_img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 100, 0), 2)
        qie_img = c_img[y:y + h, x:x + w]
    elif w == 601:
        c_img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 100, 0), 2)
        qie1_img = c_img[y:y + h, x:x + w]
# 改变图片像素
q_img=cv2.resize(qie_img,(300,200))
q1_img=cv2.resize(qie1_img,(600,300))
rs = demo01(q_img)
print(f"{rs}")
rs1 = demo01(q1_img)
print(f"{rs1}")

cv2.imshow("a", qie_img)
cv2.imshow("c", qie1_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
