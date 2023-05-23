def self(i):
    c=0
    cnt=0
    t=i
    while(i!=0):
        r=i%10
        c+=1
        if r>0:
            if t%r==0:
                cnt+=1
        i=i//10
    if(cnt==c):
        return True
    else:
        return False

a=int(input())
b=int(input())
for i in range(a,b+1):
    if self(i):
        print("%d"%(i),end=" ")