#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PIL import Image
import os
pathdir='/root'
os.chdir(pathdir)
def get_img_file():
	img_list=[]
	list_dir=os.listdir(pathdir)
	for i in list_dir:
		if '.jpg' in i:
			img_list.append(i)
		elif '.png' in i:
			img_list.append(i)
	return img_list

def resize_img(lan=100):
	for f in get_img_file():
		img=Image.open(f)
		if max(img.size) >lan:
			value=max(img.size)/100.0
			resize_img=min(img.size)/value
			newimg=img.resize((100,int(resize_img)),Image.ANTIALIAS)
			newimg.save('new_'+f)
		else:
			print("this picture is ok!")

resize_img()
