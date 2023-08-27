a=int(input())
lst=list(map(int,input().split()))
ls=list(map(int,input().split()))
for i in range(len(lst)):
    print(ls[i]+lst[i],end=' ')