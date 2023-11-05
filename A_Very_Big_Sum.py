def aVeryBigSum(ar):
    total_sum = 0
    for num in ar:
        total_sum += num
    return total_sum

# Input
n = int(input())
ar = list(map(int, input().split()))

# Calculate the sum
result = aVeryBigSum(ar)

# Output
print(result)
