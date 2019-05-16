'''
给定一个数组 A，将其划分为两个不相交（没有公共元素）的连续子数组 left 和 right， 使得：

    left 中的每个元素都小于或等于 right 中的每个元素。
    left 和 right 都是非空的。
    left 要尽可能小。

在完成这样的分组后返回 left 的长度。可以保证存在这样的划分方法。

示例 1：

输入：[5,0,3,8,6]
输出：3
解释：left = [5,0,3]，right = [8,6]

'''
import  random
from  time import  sleep
# a = []
# i = 0
# while i <= 7:
#     i +=1
#     n = random.randint(1,37)
#     if n not in a:
#         a.append(n)
#
# print(a)


# def to_weire_case(s):
#     for index,w in enumerate(s):
#         print(index,w)
#         if index%2 == 0:
#            a =  s.replace(w, w.lower())
#         else:
#            a = s.replace(w, w.upper())
#
#     print(a)
#
# a = 'This is a test'
# to_weire_case(a)

import gui_tkinter


window = gui_tkinter.Tk()
window.title('this is window')
window.geometry('300x200')


window.mainloop()