# '''
# Author: Jack.Zhou
# Date: 2024-11-14 16:55:24
# LastEditTime: 2024-11-14 17:11:47
# '''

# jack
def trim(s):
    if s[0:2] == '  ' and s[-2:] != '  ':
        s = s[2:]
        return s
    elif s[0:2] == '  ' and s[-2:] == '  ':
        s = s[2:-2]
        return s
    elif s[0:2] != '  ' and s[-2:] == '  ':
        s = s[0:-2]
        return s
    else :
        s = ''
        return s
    
# 网站答案 递归方法分别去除左右两边空格
def trim(s):
    if len(s) > 0:
        if s[0] == ' ':
            return trim(s[1:])
        elif s[-1] == ' ':
            return trim(s[:-1])
        else:
            return s
    else:
        return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败-01!')
elif trim('  hello') != 'hello':
    print('测试失败!-02')
elif trim('  hello  ') != 'hello':
    print('测试失败!-03')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!-04')
elif trim('') != '':
    print('测试失败!-05')
elif trim('    ') != '':
    print('测试失败!-06')
else:
    print('测试成功!')




