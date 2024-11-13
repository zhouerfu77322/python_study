'''
Author: Jack.Zhou
Date: 2024-11-13 16:29:01
LastEditTime: 2024-11-13 16:38:33
'''
'''
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 
ax²+bx+c=0
的两个解。
'''

import math

def quadratic(a, b, c):
    pass
    y = (b**2) - (4*a*c)
    y1 = math.sqrt(y)
    x1 = (-b + y1)/(2*a)
    x2 = (-b - y1)/(2*a)
    return x1,x2

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')