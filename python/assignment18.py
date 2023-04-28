def find_union(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    
    union_set = set1.union(set2)
    
    union_list = list(union_set)
    
    return union_list

arr1 = list(map(int, input("Enter the first array (space-separated integers): ").split()))
arr2 = list(map(int, input("Enter the second array (space-separated integers): ").split()))

union = find_union(arr1, arr2)
print("The union of the two arrays is:", union)
