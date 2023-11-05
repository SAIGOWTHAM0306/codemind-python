def find_missing_number(arr):
    n = len(arr) + 1  # Number of elements including the missing one
    expected_sum = n * (n + 1) // 2  # Sum of numbers from 1 to n using arithmetic sum formula
    actual_sum = sum(arr)  # Sum of the given array
    return expected_sum - actual_sum  # The missing number

# Example usage:
test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    array = list(map(int, input().split()))
    missing_number = find_missing_number(array)
    print(missing_number)
