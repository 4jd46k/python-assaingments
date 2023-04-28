def sum_array():
    # take input from user to create array
    arr = input("Enter elements of the array separated by space: ").split()
    
    # convert each element to int and calculate the sum
    sum = 0
    for i in arr:
        sum += int(i)
    
    # return the sum
    return sum

# call the function and print the result
result = sum_array()
print("The sum of the array is:", result)
