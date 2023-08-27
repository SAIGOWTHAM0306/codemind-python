a=int(input())
lst=list(map(int,input().split()))
pr1=1
pr=1
for i in lst:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if(c==2):
        pr=pr*i
    else:
        pr1=pr1*i
print(abs(pr1-pr))