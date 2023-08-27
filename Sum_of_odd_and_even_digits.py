a=int(input())
lst=list(map(int,input().split()))
s=0
sm=0
for i in range(len(lst)):
    if i%2==0:
        sm=sm+lst[i]
    else:
        s=s+lst[i]
if s==sm:
    print("YES")
else:
    print("NO")