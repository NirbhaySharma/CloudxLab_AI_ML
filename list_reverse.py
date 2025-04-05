lis = [1,2,3,4,3,2,4,7]

def swap(lis,index):
    temp = lis[index]
    lis[index] = lis[(len(lis)-1 - index)]
    lis[(len(lis)-1 - index)] = temp

def rev_list(lis):
    for i in range(0, len(lis)//2):
        swap(lis,i)

print(lis)
rev_list(lis)
print(lis)
