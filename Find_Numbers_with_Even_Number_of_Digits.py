def cntdigit(n):
    c=0
    while(n!=0):
        r=n%10
        c+=1
        n=n//10
    return c
a=int(input())
lst=list(map(int,input().split()))
cnt=0
for i in lst:
    ev=cntdigit(i)
    if ev%2==0:
        cnt+=1
print(cnt)