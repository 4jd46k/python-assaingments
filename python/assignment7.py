def remove_duplicates(arr):
    unique_array = []
    for element in arr:
        if element not in unique_array:
            unique_array.append(element)
    return unique_array

user_input = input("Enter elements of the array separated by a space: ")
arr = user_input.split()
arr = list(map(int, arr)) 
result = remove_duplicates(arr)
print(result)
