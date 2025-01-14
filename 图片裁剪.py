import cv2

img = cv2.imread('images/car.png')
h, w, c = img.shape
print('高', h, '宽', w, '通道', c)

# 定义坐标，原点在左上角，x，y为裁剪起始坐标，w，h为裁剪图片宽高
x = 100  # x坐标小于图片宽度
y = 100  # y坐标小于图片高度
w = 300  # w,h,裁剪后的图片像素
h = 100
cai_img = img[y:y + h, x:x + w]  # 图片截取公式
h1, w1, c1 = cai_img.shape
print('高', h1, '宽', w1, '通道', c1)
cv2.imshow('old', img)
cv2.imshow('image', cai_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
