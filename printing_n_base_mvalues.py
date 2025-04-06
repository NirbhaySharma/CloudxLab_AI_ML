import math

n = 3
m = 3

lis = []
for i in range(0 , n):
    lis.append(0)

print(lis)
print_iterations = math.pow(m,n)

def increment_val(power):
    carry = 1
    global lis
    for i in range( len(lis)-1,-1,-1):
        if(lis[i] + carry >=power):
            lis[i] = 0
            carry = 1
            if i == 0:
                lis = [1] + lis
        else:
            lis[i] = lis[i] + 1
            return lis
    return lis

for i in range(0,int(print_iterations+10)):
    print(increment_val(m))
