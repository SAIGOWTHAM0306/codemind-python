a=int(input())
for i in range(a):
    m,n,o,p=map(int,input().split())
    x=m//n
    y=m//o
    z=m//(n*o)
    if(x+y-z>=p):
        print("Win")
    else:
        print("Lose")