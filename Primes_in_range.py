def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def find_primes_in_range(start, end):
    c=0
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            c+=1
    return c

# Input range
start = int(input())
end = int(input())

prime_numbers = find_primes_in_range(start, end)
print(prime_numbers)
