import cv2


def img01():
    # 读取图片,作用，1.方便ocr文字识别，像素超过ocr阈值，识别不出来需要调整图片大小
    # 模型训练，图片大小影响模型训练的复杂度
    img = cv2.imread('images/car.png')
    if img is None:
        print('图片不存在')
        return
    # 获取图片大小
    (h, w) = img.shape[:2]
    
    print(h, w)
    # 调整大小
    r_img = cv2.resize(img, (200, 100))
    (h, w) = r_img.shape[:2]
    print(h, w)
    cv2.imshow('old', img)
    cv2.imshow('new', r_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img01()