def swap_number(a,b):
    return b,a

def shift_number(ar, count):
    for i in range (0, count):
        val = ar[0]
        del ar[0]
        ar.append(val)
    return ar

print(swap_number(2,3))

arr = [1,2,3,4]
print(shift_number(arr,2))
