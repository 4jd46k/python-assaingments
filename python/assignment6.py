def find_second_largest(arr):
    arr = list(set(arr))
    arr.sort(reverse=True)
    return arr[1]
num_str = input("Enter a list of numbers, separated by spaces: ")
num_list = [int(n) for n in num_str.split()]
second_largest = find_second_largest(num_list)
print("The second largest number is:", second_largest)
