#!/usr/bin/env python
#-*- coding:utf -*-
import re
import urllib
import time
import os

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
	reg = r'<a.*href="(.*)"'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	for i in imglist:
		if "http:" in i or "https:" in i:
			#可以直接写到txt中
			print i
		else:
			if '"' in i:
				print "http://www.w3school.com.cn"+i.split('"')[0]
			else:
				print "http://www.w3school.com.cn"+i
				
			
#    return imglist

#getImg(getHtml("http://www.w3school.com.cn/html/"))
if __name__ == '__main__':
	getImg(getHtml("http://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html"))

