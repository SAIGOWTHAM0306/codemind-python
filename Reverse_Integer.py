def reverse_integer(x):
    if x < 0:
        sign = -1
        x = -x
    else:
        sign = 1

    # Convert the integer to a string, reverse it, and remove leading zeros
    reversed_str = str(x)[::-1].lstrip('0')

    # Convert the reversed string back to an integer
    reversed_int = int(reversed_str)

    # Apply the sign to the reversed integer
    reversed_int *= sign

    # Check for integer overflow
    if reversed_int < -2**31 or reversed_int > 2**31 - 1:
        return 0

    return reversed_int

# Input
x = int(input())

# Calculate the reverse
result = reverse_integer(x)

# Output
print(result)
