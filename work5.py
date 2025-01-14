import cv2
import numpy as np
from myocr.MyUtile1 import demo01

img=cv2.imread('images/car6.png')
gay_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
k = np.ones((9, 9), np.uint8)
close_img = cv2.morphologyEx(gay_img, cv2.MORPH_TOPHAT, k)
gs_img = cv2.GaussianBlur(close_img, (9, 9), 2)
c_img = cv2.Canny(gs_img, 170,  175)
open_img=cv2.dilate(c_img,np.ones((15,15),np.uint8),iterations=3)

contours, hierarchy = cv2.findContours(open_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
num = len(contours)
print(f"长度={num }")
qie_img = 0
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if w > 160:
        a = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 100, 0), 2)
        qie_img = a[y:y + h, x:x + w]
rs = demo01(qie_img)
print(f"车牌号码是:{rs}")
cv2.imshow('gay', qie_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
