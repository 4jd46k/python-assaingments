n = int(input("Enter a number: "))
sum = 0
for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print("The sum of all the multiples of 3 or 5 below", n, "is", sum)