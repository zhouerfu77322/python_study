'''
Author: Jack.Zhou
Date: 2024-11-11 10:51:18
LastEditTime: 2024-11-13 16:40:13
'''
'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''

height = float(input('请输入你的身高(M)'))
weight = float(input('请输入你的体重(kg)'))

bmi = weight/(height**2)


if bmi <= 18.5:
    print('体重过轻')
elif bmi > 18.5 and bmi <= 25:
    print('体重正常')
elif bmi > 25 and bmi <= 32:
    print('体重过胖')
elif bmi > 32:
    print('严重肥胖')
else:
    print('请输入数字')