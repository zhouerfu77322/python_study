'''
Author: Jack.Zhou
Date: 2024-11-13 16:48:27
LastEditTime: 2024-11-13 17:06:51
'''
# def power(x,n=2):  #给到 n 一个默认参数为2
#     return x ** n
# power(5)

# # 顺序参数
# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)

# enroll('jack','F',city='chengdu',age=18) #不按顺序调用
# enroll('jason','M',city='zigong') #不按顺序调用+使用默认参数

# 可变参数
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print(calc(1,2))
# print(calc())

# 练习:以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def mul(x,*args):
    n = x
    for i in args:
        n = n * i
    

    
    return n
# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5,6))
print('mul(5, 6, 7) =', mul(5,6,7))
print('mul(5, 6, 7, 9) =', mul(5,6,7,9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')