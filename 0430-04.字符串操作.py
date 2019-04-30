#coding=utf-8
#字符串的索引
s='baidu'
print(s[0])
print(s[3])
print(s[-1])
print(s[-4])

#字符串的切片,切片时string[x,y]候截取的信息x,y-1
s='www.baidu.com'
print(s[3:])
print(s[:-3])
print(s[4:-4])
print(s[4:9])

#字符串的拼接
a='heygor '
b='handsome!!'
print(a+b)
print(a,b)
c=str(19)
print(a+c)

#字符串的遍历
for i in a:
    print(i)

#字符串去空格
#strip()   去掉两边的空格
#lstrip()  去掉左边空格
#rstrio()  去掉右边空格
s='    test    '
print(s.strip())
print(s.lstrip())

#计算字符串长度
#len()函数
print(len(s))


#引号
print('im heygor')
print("im heygor")
print('''im heygor''')

#print('i'm your baba')
print("i'm your papa")

print('''
名字:heygor
年龄:20
''')

















