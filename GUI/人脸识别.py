import os

import cv2
import face_recognition
import numpy as np
import mysql
import PySimpleGUI as sg


def dataget():
    # 开摄像头
    cap = cv2.VideoCapture(0)
    if cap.isOpened() == False:
        print('摄像头没开')
        return
        #
    layout = [
        [sg.Text('编号：'), sg.InputText(key='num')],
        [sg.Text('姓名'), sg.InputText(key='name')],
        [sg.Image(key='video')],
        [sg.Button('关闭'), sg.Button('人脸识别'), sg.Button('人脸采集')]

    ]

    window = sg.Window('人脸识别', layout)

    while True:
        event, values = window.read(timeout=10)
        ret, frame = cap.read()
        if event in (None, '关闭'):
            break
        if ret:
            imgType = cv2.imencode('.png', frame)[1].tobytes()
            window['video'].update(data=imgType)
        if event == '人脸采集':
            # 获取编号姓名
            num = values['num']
            name = values['name']
            # 写入人脸图片
            iss = cv2.imwrite(f'D:\\images\\{num}.png', frame)
            if iss:
                isAdd = mysql.add(name, num)
                if isAdd:
                    sg.popup('人脸采集成功')
            else:
                sg.popup('人脸采集失败')
        if event == '人脸识别':
            list_dir = os.listdir("D:\\images")
            if len(list_dir) > 0:
                for i in list_dir:
                    img = cv2.imread(f"D:\\images\\{i}")
                    if img is None:
                        print('没有读取到图片')
                        break
                    else:
                        # 获取已知图片的特征变量
                        en1 = face_recognition.face_encodings(img)[0]
                        en2 = face_recognition.face_encodings(frame)[0]
                        rs = np.linalg.norm(en1 - en2)
                        print(rs)
                        if rs < 0.5:
                            b = i.split(".")[0]
                            a = mysql.query(b)
                            sg.popup(f'这是{a}')
                            break
                        elif 0.5 < rs < 0.55:
                            b = i.split(".")[0]
                            a = mysql.query(b)
                            sg.popup(f'这可能是{a}')
                            break
                        else:
                            sg.popup('数据库中没有此人')
    cap.release()
    window.close()


if __name__ == '__main__':
    dataget()
