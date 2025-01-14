import os
import face_recognition
import numpy as np
import Sql
import PySimpleGUI as sg
import cv2


def character_recognition():
    # 设置主题
    sg.theme('LightBlue')
    # 布局定义
    layout = [
        [sg.Text('请选择一张图片:')],
        [sg.Input(key='SC', enable_events=True),
         sg.FileBrowse(file_types=(("Image Files", "*.png"),))],
        [sg.Button('关闭'), sg.Button('识别')],
        [sg.Image(key='image', )]
    ]

    # 创建窗口
    window = sg.Window('人脸识别', layout)

    while True:
        event, values = window.read()
        # 处理事件
        if event in (None, '关闭'):
            break
        if event == 'SC':
            # 更新图片,图片路径不能有中文
            image_path = values['SC']
            if image_path:
                # 转换，
                r_img =cv2.imread(image_path)
                img = cv2.resize(r_img, (400, 300))
                imgType = cv2.imencode(".png", img)[1].tobytes()
                window['image'].update(data=imgType)
            img1 = cv2.imread(image_path)
            gray_image1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            list_dir = os.listdir("gay_images")
            # print(list_dir)
            a = cv2.imwrite(fr'./gay_images/{len(list_dir) + 1}.png', gray_image1)
            # print(a)
            # 使用高斯滤波去除噪声
            gs_img1 = cv2.GaussianBlur(gray_image1, (3, 3), 0)
            image1 = cv2.cvtColor(gs_img1, cv2.COLOR_GRAY2BGR)
            face_locations1 = face_recognition.face_locations(image1)
            # 提取人脸特征码
            # print(face_recognition.face_encodings(image1))
            if len(face_recognition.face_encodings(image1)) == 0:
                sg.popup('数据库中没有读取到该人物图片')
                continue

            face_encodings1 = face_recognition.face_encodings(image1)[0]

        if event == '识别':
            list_dir = os.listdir("D:\\images")
            if len(list_dir) == 0:
                sg.popup("库中图片为空")
                break
            if len(list_dir) > 0:
                for i in list_dir:
                    img2 = cv2.imread(f"D:\\images\\{i}")
                    if img2 is None:
                        sg.popup('没有读取到图片')
                    else:
                        gray_image2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
                        # 使用高斯滤波去除噪声
                        gs_img2 = cv2.GaussianBlur(gray_image2, (3, 3), 0)

                        image2 = cv2.cvtColor(gs_img2, cv2.COLOR_GRAY2BGR)
                        # 读取人脸位置
                        face_locations2 = face_recognition.face_locations(image2)
                        # 提取人脸特征码
                        face_encodings2 = face_recognition.face_encodings(image2)[0]
                        # 获取已知图片的特征变量t
                        try:
                            rs = np.linalg.norm(face_encodings1 - face_encodings2)
                            if rs < 0.5:
                                b = i.split(".")[0]
                                a = Sql.query(b)
                                sg.popup(f'这是{a}')
                                break
                            else:
                                pass
                        except NameError as e:
                            sg.popup(f'这是非人物图片')
                            break
    window.close()


if __name__ == '__main__':
    character_recognition()
