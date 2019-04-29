#coding=utf-8
#补充:type可以查看变量的数据类型
'''
数据类型的转换
int()    数据转换为数字类型数据
str()    数据转换为字符类型数据
float()  数据转换为浮点类型数据
'''


age=int(input('请输入您的年龄'))
print(type(age))

if age>10:
    print('来开黑呀！！！！')
else:
    print('请你放弃游戏，让我们活几天吧')
