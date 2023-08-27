a=int(input())
lst=list(map(int,input().split()))
ls=[]
for i in lst:
    c=i*i
    ls.append(c)
lis=sorted(ls)
for i in range(len(lis)):
    print(lis[i],end=' ')