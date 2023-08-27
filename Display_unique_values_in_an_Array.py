a=int(input())
lst=list(map(int,input().split()))
ls=[]
fl=0
for i in range(len(lst)):
    c=0
    for j in range(len(lst)):
        if lst[i]==lst[j]:
            c+=1
    if c==1:
        fl=1
        ls.append(lst[i])
if fl==0:
    print(-1)
else:
    for i in range(len(ls)):
        print(ls[i],end=' ')