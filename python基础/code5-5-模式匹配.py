'''
Author: Jack.Zhou
Date: 2024-11-11 16:46:25
LastEditTime: 2024-11-13 16:40:02
'''
args = 'jack'
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case 'gcc':
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case 'jason':
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case 'jack':
        print('clean')
    case _:
        print('invalid command.')