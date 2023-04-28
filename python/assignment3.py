def sort_numbers():
    numbers = input("Enter a list of numbers, separated by spaces: ").split()
    numbers = [int(num) for num in numbers]
    sorted_numbers = sorted(numbers)
    return sorted_numbers
sorted_nums = sort_numbers()
print(sorted_nums)
