a=int(input())
lst=list(map(int,input().split()))
for i in range(len(lst)):
    c=0
    for j in range(len(lst)):
        if lst[i]>lst[j]:
            c+=1
    print(c,end=' ')