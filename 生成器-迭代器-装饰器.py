#生成器

# g = (x for x in range(10))
# print(g)
# next(g)
# for i in g:
#     print(i)

#迭代器
# def g(x):
#     for i in range(x):
#         print(i)
#         yield i
#
# a = g(2)
# print(g(2))
# def check_password(func):
#     def inner():
#         print('密码验证中.....')
#         func()
#     return inner
# @check_password
# def deposit():
#     print('存款中......')
#
# def withdrawal():
#     print('取款中......')
#
#
# deposit = check_password(deposit)
# print(deposit)
def hi(func):
    def inner():
        func()
        print('hello.....')
    return inner

@hi
def people():
    print('hulk')

def people2():
    print('alan')


people()

