#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open(r'C:\Users\wangxinguo\Desktop\garcia-txt\\9.jpg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save(r'C:\Users\wangxinguo\Desktop\garcia-txt\\blur.jpg', 'jpeg')
