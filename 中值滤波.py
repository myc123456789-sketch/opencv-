import cv2

img = cv2.imread('images/hujiao.png')

# 定义中值滤波，滤波的孔径,是奇数
c = 5
# 中值滤波
m_img=cv2.medianBlur(img,c)

cv2.imshow('img',img)
cv2.imshow('m_img',m_img)
cv2.waitKey(0)
cv2.destroyAllWindows()