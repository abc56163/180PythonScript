#一个HTML文件，找出里面的正文,找出里面的链接

import requests
from lxml import etree

def get_html():
    text = requests.get('http://news.youth.cn/gn/201812/t20181229_11829901.htm').content.decode('gb2312')
    html = etree.HTML(text)
    txt = html.xpath('/html/body/div[1]/div[2]/div/div[3]/div[1]/div/p/text()')
    img = html.xpath('/html/body/div[1]/div[2]/div/div[3]/div[1]/div/p/img/@src')
    print(img)


get_html()



