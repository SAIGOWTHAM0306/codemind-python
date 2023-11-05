p,r,t=map(int,input().split())
r/=100
interest=p*((1+r)**t)
print(f"{interest:.2f}")
