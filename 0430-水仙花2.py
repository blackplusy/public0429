#coding=utf-8
for a in range(100,1000):
    b=a//100
    c=a%100//10
    d=a%10
    # if b**3+c**3+d**3==a:
    #     print('水仙花数字',a)
    if (a//100)**3+(a%100//10)**3+(a%10)**3==a:
    	print('水仙花数字',a)


