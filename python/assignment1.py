def find_max(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val
arr = []
n = int(input("Enter the number of elements in the array: "))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)
max_val = find_max(arr)
print("The maximum value is:", max_val)
