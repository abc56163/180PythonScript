#用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)

import requests
from lxml import etree
import string
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
def mz_url():
    text = requests.get('http://tieba.baidu.com/p/2166231880',headers).content
    html = etree.HTML(text)
    imgs = html.xpath('//div[@id="post_content_29397251028"]/img[@class="BDE_Image"]/@src')
    return imgs

def mz_img():
    imgs = mz_url()
    for index,img in enumerate(imgs):
        text = requests.get(img,headers)
        with open('/root/Desktop/mzimg/%s.jpg' %index ,'wb')as fb:
            for i in text.iter_content(chunk_size=1024):
                fb.write(i)

mz_img()





