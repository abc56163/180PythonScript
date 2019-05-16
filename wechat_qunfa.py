import itchat
import sys
import time
from threading import Thread
def qunfa(massage):
    UserNames = itchat.get_friends(update=True)[1:]
    for index,name in  enumerate(UserNames):
        username = name['UserName']
        remarkname = name['RemarkName']
        nickname = name['NickName']
        for m in massage.split('，'):
            itchat.send(m, toUserName='{}'.format(username))
            time.sleep(4)
        if remarkname == '':
            print(index,nickname, '发送成功')
        else:
            print(index,remarkname, '发送成功')
        time.sleep(1)


@itchat.msg_register('Text')
def sendmassage(msg):
    user = msg['User']
    def _send(massage):
        for m in massage.split('，'):
            itchat.send(m, msg['FromUserName'])
            time.sleep(4)

    if user['RemarkName'] == '':
        print(user['NickName'],msg['Content'])
    else:
        print(user['RemarkName'],msg['Content'])
    if '新年好' in msg['Content']:
        _send(massage)
    elif '猪年' in msg['Content']:
        _send(massage)
    elif '过年' in msg['Content']:
        _send(massage)
    elif '新年快乐' in msg['Content']:
        _send(massage)
    elif '新年' in msg['Content']:
        _send(massage)
    elif '祝福' in msg['Content']:
        _send(massage)
    elif '春节' in msg['Content']:
        _send(massage)
    elif '2019年' in msg['Content']:
        _send(massage)
    elif msg['Content'] == '990520':
        qunfa(massage)



if __name__ == '__main__':
    massage = '祝老板你在2019这新的一年里\n[福]福从天降[福]，/:rose好运连连/:rose，[红包]财源滚滚[红包]，[福]大吉大利[福]，🎉📦新年发发发🎉📦'
    itchat.auto_login(True)
    itchat.run()



