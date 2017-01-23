#!/usr/bin/env python
#-*- coding:utf-8 -*-
import random
import sys
import MySQLdb as mysql
import uuid
global cur,conn,some_list
some_list=[]
#############################
#生成字符串一
def str_random(length=8,some=10):
	a='1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	list2=[]
	for j in range(some):
		list1=[]
		for i in range(length):
			list1.append(random.choice(a))
		list2.append(''.join(list1))
	return list2
#生成字符串二
def str2_random(length=8):
    list=[]
    for i in range(10):
       list.append(str(i))
    for i in range(65,91):
       list.append(chr(i))
    for i in range(97,123):
       list.append(chr(i))
    return ''.join(random.sample(list,length))
#生成字符串三(只有小写字母)
def str3_random(length=8):
	return str(uuid.uuid4()).replace('-','')[:length]
#try:
#	if type(int(sys.argv[1])) is int:
#		print str_random(int(sys.argv[1]))
#except Exception,e:
#	print Exception,":",e
###################################################################################################
#如下是写入到数据库中
############################################################################################
def db_random(list=[]):
    try:
        conn=mysql.connect(host='localhost',port=3306,user='root',passwd='123123',db='test',charset='utf8')
        cur=conn.cursor()
	for i in list:
		cur.execute('insert into random values(%s)',i)
	print "写到localhost test数据库,random表中:"
	print list
	conn.commit()
	cur.close()
	conn.close()
    except mysql.Error,e:
	print "mysql error %d:%s" %(e.args[0],e.args[1])
##############################################################################################
if __name__ == '__main__':
	db_random(str_random())

###############################################################################################
