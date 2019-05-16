'''
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
包括空行和注释，但是要分别列出来。
'''
with open('单词打印.py','r') as fb:
    codes = fb.read()
    code_nu = 0
    zs_nu = 0
    space = 0
    for code in codes.split('\n'):
        if '#' in code:
            zs_nu +=1
        elif code == '':
            space +=1
        else:
            code_nu +=1

print('代码行数:{}\n注释行数:{}\n空格行数:{}'.format(code_nu,zs_nu,space))