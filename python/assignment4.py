def sum_even_numbers(n):
    sum = 0
    for i in range(2, n+1, 2):
        sum += i
    return sum
n = int(input("Enter a positive integer: "))
result = sum_even_numbers(n)
print(f"The sum of all even numbers between 1 and {n} is {result}")
