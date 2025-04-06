num = 0
power = 5

def multiply(x,y):
    sum = 0
    val = '+'
    if (x <0 and y >0) or (x >0 and y < 0) :
        val = '-'

    for i in range(0,abs(y)):
        sum += abs(x)
    if val == "+":
        return sum
    else:
        return -sum

def pow_cust(num, power):
    if power % 1 != 0:
        return -1
    if power == 0:
        return 1
    numb = num
    for i in range(0 , power-1):
        numb = multiply(numb,num)
    return numb


print(pow_cust(num,power))
