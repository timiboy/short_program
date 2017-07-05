# -*- coding: utf-8 -*-
from PIL import Image
import time
import pytesseract

def captcha_recognition(img_name):
    img = Image.open(img_name)
    width, height = img.size
    box = (2, 2, width-2, height-2)
    new_img = img.crop(box)
    r, g, b = new_img.split()
    new_img = new_img.convert('L')
    gray_img = new_img.point(lambda i: 0 if i<140 else 255)
    gray_img.show()
    gray_img.save('gray_'+img_name)
    config = '-psm 7'  #声明只有一行内容
    captcha = pytesseract.image_to_string(gray_img, config=config)
    print(captcha)

if __name__ == "__main__":
    captcha_recognition('7556.jpg')

