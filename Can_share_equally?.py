x,y=map(int,input().split())
if x%2==0 and y%2==0:
    print("YES")
elif x%2==0 and x!=0 and y%2!=0:
    print("YES")
else:
    print("NO")