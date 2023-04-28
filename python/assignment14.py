n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib = [0, 1]
for i in range(2, n):
    next_fib = fib[i-1] + fib[i-2]
    fib.append(next_fib)
print(fib)
