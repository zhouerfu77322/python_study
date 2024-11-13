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