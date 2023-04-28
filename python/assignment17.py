num = int(input("Enter a number: "))
choice = input("Do you want to find the sum of even or odd numbers? Type 'even' or 'odd': ")

sum = 0
current_num = 0

while current_num < num:
    if choice == "even" and current_num % 2 == 0:
        sum += current_num
    elif choice == "odd" and current_num % 2 != 0:
        sum += current_num
    current_num += 1

print("The sum of", choice, "numbers below", num, "is", sum)
