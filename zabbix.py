import sys
import requests
import json


class Zabbix:
    def __init__(self,corpid,corpsecret):
        self.corpid = corpid
        self.corpsecret = corpsecret


    def access_token(self,corpid, corpsecret):
        token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + corpsecret
        req = requests.get(token_url).text
        token = json.loads(req)['access_token']
        return token

    def sendmessage(self,message):
        token = self.access_token(corpid, corpsecret)
        url = ' https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + token
        msg = json.dumps(message)
        response = requests.post(url, msg)
        print(response.text)


if __name__ == '__main__':

    corpid = 'ww20372d589e9dc441'
    corpsecret = 'hvVzh77X5H908o5IK44jl5UasS6SGKR2efw0HaBBaKw'
    appsecret = '1000002'
    userid = "touser"
    partyid = 2

    message = {
        "touser": userid,
        "toparty": partyid,
        "msgtype": "text",
        "agentid": appsecret,
        "text": {
            'content': sys.argv[1]
        },
        "safe": 0
    }

    zabbix = Zabbix(corpsecret,corpid)
    zabbix.sendmessage(message)