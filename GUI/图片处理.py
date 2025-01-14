import os

import PySimpleGUI as sg
import cv2
from PIL import Image


def main():
    # 设置主题
    sg.theme('LightBlue')
    # 布局定义
    layout = [
        [sg.Text('请选择一张图片:')],
        [sg.Input(key='SC', enable_events=True),
         sg.FileBrowse(file_types=(("Image Files", "*.png;*.jpg;*.jpeg;*.gif"),))],
        [sg.Button('关闭'), sg.Button('上传')],
        [sg.Image(key='image')]
    ]
    # 创建窗口
    window = sg.Window('文件处理', layout)
    while True:
        event, values = window.read()
        # 处理事件
        if event in (None, '关闭'):
            break
        if event == 'SC':
            # 更新图片,图片路径不能有中文
            image_path = values['SC']
            print(image_path)
            img = cv2.imread(image_path)
            imgType = cv2.imencode('.png', img)[1].tobytes()
            window['video'].update(imgType)
            if image_path:
                window['image'].update(filename=image_path)
            # if image_path:
            #     image = Image.open(image_path)
            #     image.save(image_path[0:-4] + ".png", 'PNG')
            #     # 把文件路径重新传给sg.Image filename 不支持jpg格式版本不同 转为png就可以忽略版本问题
            #     window['image'].update(filename=image_path[0:-3] + 'png')
            #     if os.path.exists(image_path) and image_path[::-1][0:3] != "png":
            #         # 删除文件
            #         os.remove(image_path)
    window.close()


if __name__ == '__main__':
    main()
