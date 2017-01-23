#/bin/env bash
#-*- coding:utf-8 -*-

./pachong_getgirls_image.py

cd /opt/sources/img/python
a=`find . -type d|grep "./"|awk -F '/' '{print $2}'`
for i in $a
do
	\cp -r index.html $i/
done
