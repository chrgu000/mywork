#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re
import urllib
import time
import os
list=[]
def readfile(text):
	f=open(text,'r')
	lines=f.readlines()
	f.close()
	return lines

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'class="BDE_Image" src="(.*\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist      
   
def url_download(url,path,filename):
	connect=urllib.urlopen(url)
	if os.path.exists(path) is not True:
		os.mkdir(path)
	name=path+"/picture"+filename+".jpg"
	f=open(name,'wb')
	f.write(connect.read())
	f.close()
	print(name+" picture saved!")

def pachong():
    filelist=readfile("pachong_getgirls_image.txt")
    for url in filelist:
	#一个页面，一个时间生成的目录
	print "本次爬虫的网址是:"+url
	html = getHtml(url)
	list1=getImg(html)
	path1="/opt/sources/img/python/"+time.strftime("%Y-%m-%d_%H_%M_%S")

	flag=0
	for i in range(len(list1)):
		a=list1[i]
		for j in a.split('"'):
			if "jpg" in j:
				url_download(j,path1,str(flag))
				flag=flag+1
if __name__=='__main__':
	pachong()
