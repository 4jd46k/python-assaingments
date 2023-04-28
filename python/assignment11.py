def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

limit = int(input("Enter the limit: "))

prime_sum = 0
for num in range(2, limit+1):
    if is_prime(num):
        prime_sum += num

print("The sum of all prime numbers up to", limit, "is", prime_sum)
