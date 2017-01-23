#!/usr/bin/env python
#! -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random,numpy,string

def code_image(path="/opt/sources/img"):
# generate 4 ramdom letters
	text = random.sample('0123456789'+string.letters,4)
	#新建一个三维数组
	rawArray = numpy.zeros((100,300,3),dtype=numpy.uint8)
	sh = rawArray.shape
	for i in range(sh[0]):
	    for j in range(sh[1]):
	        for k in range(sh[2]):
	            #取到各种灰度级，作为背景颜色
	            rawArray[i][j][k]=random.randrange(50,255,30)
	#初始化背景颜色
	im = Image.fromarray(rawArray)
	draw = ImageDraw.Draw(im)
	#在背景图片上面加上字母或数字
	for i in range(len(text)):
	    draw.text((75*i+random.randint(0,40),random.randint(0,40)), text[i],font=ImageFont.truetype("FRAMDIT.TTF",60),fill = (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
	#在背景图片上加两条横线
	draw.line([10+random.randint(0,40),10+random.randint(0,20),200+random.randint(0,40),10+random.randint(0,20)],"red")
	draw.line([70+random.randint(0,40),50+random.randint(0,20),270+random.randint(0,40),50+random.randint(0,20)],"green")
	draw.rectangle((10,10,280,80),outline = "yellow")
	im.save(path+"/checkcode.jpg")

if __name__ == '__main__':
	code_image()
