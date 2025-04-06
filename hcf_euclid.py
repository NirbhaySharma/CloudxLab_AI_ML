num1 = 272
num2 = 42

def euc(num1,num2):
    if num1 < num2:
        if num2 % num1 == 0:
            return num1
        else:
            euc(num1,int(num2%num1))
    else:
        if num1 % num2 == 0:
            return num2
        else:
            return euc(num2,int(num1%num2))

print(euc(16,6))
