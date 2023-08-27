a=int(input())
lst=list(map(int,input().split()))
b=int(input())
flag=1
for i in range(len(lst)):
    if lst[i]==b:
        flag=0
        print(i)
        break
if flag==1:
    print(-1)