'''
 1.敏感词文本文件 filtered_words.txt，
 里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，
 否则打印出 Human Rights。
2. 敏感词文本文件 filtered_words.txt，
里面的内容 和 0011题一样，当用户输入敏感词语，
则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
'''
def auth():
    with open('filtered_words.txt','r') as fp:
        texts = fp.read()
    con =True
    print("*" * 30)
    print("input 'q' exit" )
    print("*" * 30)

    while con:
        text = input('input somthing:')
        if text == 'q':
            con = False
        else:
            for i in texts.split():
                if i in text:
                    txt = text.replace(i,'**')
                    print('Freedom:%s'% txt)
                    break
            else:
                print('Human Rights:%s' % text)


auth()