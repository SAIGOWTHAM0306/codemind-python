n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(n):
    if arr[i]!=0:
        arr[c],arr[i]=arr[i],arr[c]
        c+=1
print(*arr)