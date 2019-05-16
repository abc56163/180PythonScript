# 题目：输入某年某月某日，判断这一天是这一年的第几天？

months = (0,31,59,90,120,151,181,212,243,273,304,334)

day = int(input('day:'))
month = int(input('months:'))
year = int(input('year:'))

dsum = 0

if 0 < month < 12:
    dsum = months[month-1]
    dsum += day
else:
    print('data error')

leap = 0

if year % 400 == 0 and year % 4 ==0 and year%100 !=0:
    leap = 1

if leap == 1 and month > 2:
    dsum += 1

print('这是本年第:',dsum)



