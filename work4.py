import cv2
import numpy as np

img = cv2.imread('images/shenfen03.jpg')
gay_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
k = np.ones((3, 3), np.uint8)
close_img = cv2.morphologyEx(gay_img, cv2.MORPH_BLACKHAT, k)
k1 = (7, 7)
d = 2
gs_img = cv2.GaussianBlur(close_img, k1, d)
c_img = cv2.Canny(gs_img, 50,  100)
open_img = cv2.dilate(c_img, np.ones((7, 7)), iterations=1)
contours, hierarchy = cv2.findContours(open_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
num = len(contours)
print(f"长度={num }")
qie_img = 0
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if w > 200:
        c_img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 100, 0), 2)
        qie_img = c_img[y:y + h, x:x + w]
cv2.imshow("a", qie_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
