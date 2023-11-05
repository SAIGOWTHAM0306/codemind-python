def find_largest_digit(n):
    # Convert the number to a string to iterate through its digits
    num_str = str(n)

    # Initialize the maximum digit as 0
    max_digit = 0

    # Iterate through the digits in the string
    for digit in num_str:
        if int(digit) > max_digit:
            max_digit = int(digit)

    return max_digit

# Input
n = int(input())

# Calculate the largest digit
largest_digit = find_largest_digit(n)

# Output
print(largest_digit)
