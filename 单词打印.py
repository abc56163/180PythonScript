# 从一个英文的纯文本文件，统计其中的单词出现的个数。
# 你有一个目录，放了你一个月的日记，都是 txt，
# 为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词(do)。

with open('words.txt','r') as fp:
    words = fp.read()
    list = []
    num = 0
    for word in words.split():
        if word == 'Do':
            num +=1
        list.append(word)

    print(len(list),num)