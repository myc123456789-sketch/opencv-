import paddlehub as pub


#识别图片的文字
#img 图片含有一组文字
def demo01(img):
    #加载模型
    ocr = pub.Module(name="chinese_ocr_db_crnn_server")
    #识别文字
    rs = ocr.recognize_text(images=[img])
    return rs[0]["data"][0]["text"]
