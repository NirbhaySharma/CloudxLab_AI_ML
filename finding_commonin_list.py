arr1= [1,2,3]
arr2 = [1,3]

def find_common(arr1,arr2):
    return [i for i in arr1 if i in arr2]

print(find_common(arr1,arr2))
