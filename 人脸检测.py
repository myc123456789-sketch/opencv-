import cv2
import face_recognition
image = cv2.imread('images/p1.png')
#读取人脸位置
face_locations = face_recognition.face_locations(image)
print(face_locations)
qg_image=0
for (top, right, bottom, left) in face_locations:
    # 画出人脸区域
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    qg_image = image[top:bottom, left:right]
# 显示结果
cv2.imshow("Detected Faces", image)
cv2.imshow("QG", qg_image)
cv2.waitKey(0)
cv2.destroyAllWindows()