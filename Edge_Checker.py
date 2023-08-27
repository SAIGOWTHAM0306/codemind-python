a,b=map(int,input().split())
if a+1==b or a-1==b:
    print("Yes")
elif b+1==a or b-1==a:
    print("Yes")
elif a==10 and b==1:
    print("Yes")
elif a==10 and b==9:
    print("Yes")
elif b==10 and a==1:
    print("Yes")
else:
    print("No")
    