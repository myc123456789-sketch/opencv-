import cv2
import numpy as np
from myocr.MyUtile1 import demo01
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# # 设置窗口大小，image窗口名称，和namedWindow的窗口名称一致
# cv2.resizeWindow('image', 500, 300)
img = cv2.imread("images/wenzi01.jepg")
# gay_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# k = np.ones((3, 3), np.uint8)
# close_img = cv2.morphologyEx(gay_img, cv2.MORPH_BLACKHAT, k)

# cv2.imshow("a", img)
# cv2.imshow("image", close_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
rs = demo01(img)
print(f"车牌号码是:{rs}")
