#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import getpass
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = os.urandom(8) # 64 bits.

    assert 8 == len(salt)
    assert isinstance(salt, str)

    if isinstance(password, unicode):
        password = password.encode('UTF-8')

    assert isinstance(password, str)

    result = password
    for i in xrange(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result

#验证函数:
def validate_password(hashed,input_password):
	return hashed == encrypt_password(input_password, salt=hashed[:8])

def login(): 
	hashed=encrypt_password('123123')
	if validate_password(hashed,getpass.getpass("请输入密码:")) is True:
		print("密码正确")
	else:
		print("密码错误")
	
if __name__ == '__main__':
	login()
