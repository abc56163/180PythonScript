with open('2.txt', 'r')as passw:
   for i in passw:
       u,p=i.strip().split("|")

def login():
    n = 0
    while True:
        username = input('please input your name:')
        password = input('please input your password:')
        if username==u and password==p:
            print("登陆成功")
            break
        else:
            print("登陆失败，用户名或者秘密错误")
            n += 1
            if n >= 3:
                print('输入次数过多，已被锁定请稍后在试')
                break
login()







