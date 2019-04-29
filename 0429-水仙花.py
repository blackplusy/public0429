#coding=utf-8
a=int(input('请输入一个三位数'))
#百位
print(a//100)

#十位
print(a%100//10)

#各位
print(a%10)

b=a//100
c=a%100//10
d=a%10

if b**3+c**3+d**3==a:
    print('水仙花')
else:
    print('不是')
