'''
Author: Jack.Zhou
Date: 2024-11-13 16:48:27
LastEditTime: 2024-11-13 17:06:51
'''
def power(x,n=2):  #给到 n 一个默认参数为2
    return x ** n
power(5)

# 顺序参数
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('jack','F',city='chengdu',age=18) #不按顺序调用
enroll('jason','M',city='zigong') #不按顺序调用+使用默认参数