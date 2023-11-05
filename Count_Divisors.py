l,k,r=map(int,input().split())
c=0
for i in range(l,k+1):
    if i%r==0:
        c+=1
print(c)