#coding=utf-8

for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if (a!=b) and (b!=c) and (c!=a):
                print('%d%d%d'%(a,b,c))
