# Input: Number of registration codes (N)
N = int(input())

# Input: Registration codes as a list
registration_codes = list(map(int, input().split()))

# Initialize counters for even and odd codes
even_count = 0
odd_count = 0

# Count the even and odd codes
for code in registration_codes:
    if code % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Output: Display the count of even and odd codes
print(even_count, odd_count)
