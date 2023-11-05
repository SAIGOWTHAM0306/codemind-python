# Input: Read the length of the array (N)
N = int(input())

# Input: Read the array of digits
digits = list(map(int, input().split()))

# Initialize a carry variable to add 1 to the digits
carry = 1

# Iterate through the digits in reverse order
for i in range(N - 1, -1, -1):
    # Add the carry to the current digit
    digits[i] += carry
    # Update the carry for the next iteration
    carry = digits[i] // 10
    # Update the current digit to the remainder after dividing by 10
    digits[i] %= 10

# If there is still a carry, insert it at the beginning of the list
if carry:
    digits.insert(0, carry)

# Output: Display the updated array of digits
print(*digits)
