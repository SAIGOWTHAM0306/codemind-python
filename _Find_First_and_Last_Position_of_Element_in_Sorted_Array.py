a=int(input())
lst=list(map(int,input().split()))
b=int(input())
flag=1
ls=[]
for i in range(len(lst)):
    if lst[i]==b:
        flag=0
        ls.append(i)
if flag==1:
    print('-1 -1')
else:
    print(ls[0],ls[-1])