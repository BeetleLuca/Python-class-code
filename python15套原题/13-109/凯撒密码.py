
import math
import random
import os

#定义加密函数，对字母进行加密，即向后移动key位，其他字符不加密。
def cipher(befmessage, key):
    aftmessage = ''
    for char in befmessage:
        if char.isupper():    #对大写字母进行加密
            code = ord('A')+(ord(char)-ord('A')+key) % 26
            aftmessage = aftmessage+chr(code)
        elif char.islower():  #对小写字母进行加密
            code = __①__+(ord(char) - ord('a') + key) % 26
            aftmessage = __②__+chr(code)
        else:
            aftmessage = aftmessage+char#字母以外的其他字符不进行加密
    return aftmessage

#主程序
message = input('请输入明文：')
key = __③__(input('请输入密钥（整数）：'))  # 输入数字密钥
secret = cipher(message, __④__)
print('加密后的密文是：', __⑤__)

# 结束
