#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
filter.txt 记录敏感词汇
只要输入的词属于敏感词汇，就用**代替
-----------------------------------
2017-01-23 10:23
例如
plases input words:sex 你妹的啊大爷的love
** **的啊**的**
'''

def filterwords(u_input):
	words=[]
	r_words=[]
	f=open("filter.txt",'r')
	f_read=f.readlines()
	for i in  f_read:
		words.append(i.decode('utf-8'))
	for j in range(len(words)):
		word=f_read[j].strip()
		if word in u_input:
			r_words.append(word)
	f.close()
	return r_words

def filter():
	user_input=raw_input('plases input words:')
	user_input=user_input.replace(' ','')
	return_word=filterwords(user_input)
	if len(return_word) != 0:
		for i in return_word:
			new_input=user_input.replace(i,"**")
			user_input=new_input
	else:
		new_input=user_input

	print new_input

if __name__ == '__main__':
	filter()
