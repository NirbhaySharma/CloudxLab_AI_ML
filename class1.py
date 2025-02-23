#Initializations
base = 13    # base value
count = 15  # Total numbers to be printed in your base system
new_base = 7  # New Base  one base to another base conversion
num1 = 25  # First number
num2 = 20   # Second number
num2_base10 = num2
symbols= "0123456789abcdef"[:base]



#Functions
def base10_to_baseN(num: int,base: int) -> str:

    val = ''
    val += symbols[num % base]
    check = num // base
    if check < base:
        if(check == 0):
            return val
        val += symbols[check]
        return val[::-1]
    else:
        recur = base10_to_baseN(check,base)[::-1]
        val += recur
        return val[::-1]

def addition(num1: str,num2: str,base : int) -> str:
    leng = None
    if len(num1) > len(num2) :
        leng = len(num1)
        num2 = '0'*(len(num1)-len(num2)) + num2
    else:
        leng = len(num2)
        num1 ='0'*(len(num2)-len(num1)) + num1
    carry = 0
    res = ''
    for i in range(1, leng+1):
        val = base10_to_baseN(symbols.index(num1[-1*i]) + symbols.index(num2[
                                                                       -1*i]) + carry,
                              base)
        res = val[-1] + res
        if(len(val) == 2):
            carry = 1
        else: carry = 0
    if(carry != 0):
        res = str(carry) + res
    return res



def multiplication(num1 : int,num2_base10 : int , base : int) -> str :
     answer= 0
     for i in range(0,num2_base10):
         answer = int(addition(answer,num1,base))

     return str(answer)

def base10Converter(num1 :int , base : int) -> int:
    num1 = str(num1)
    sum = 0
    for i in range(1,len(num1) + 1):
        sum += int(num1[i *(-1)]) * base**(i-1)
    return sum


def base_n_converter(num1 : int, base : int,new_base : int):
    num1 = str(num1)
    sum = 0
    for i in range(1,len(num1) + 1):
        sum += int(num1[i *(-1)]) * base**(i-1)
    return base10_to_baseN(sum,new_base)


def base_n_subtract(num1, num2, base):
    if base < 2 or base > 10:
        raise ValueError("Base must be between 2 and 10.")

    # Define the characters used in the given base
    digits = '0123456789'[:base]

    # Ensure both numbers are of the same length by padding the shorter one with leading zeros
    max_length = max(len(num1), len(num2))
    num1 = num1.zfill(max_length)
    num2 = num2.zfill(max_length)

    # Result of subtraction
    result = []
    borrow = 0  # To keep track of any borrowing during subtraction

    for i in range(max_length - 1, -1, -1):  # Start from the rightmost digit
        # Get the numerical value of the digits in the current place
        digit1 = digits.index(num1[i])
        digit2 = digits.index(num2[i])

        # Perform the subtraction with the borrow
        diff = digit1 - digit2 - borrow

        if diff < 0:
            # Borrow from the next higher place value
            diff += base
            borrow = 1
        else:
            borrow = 0

        # Append the result digit (in character form) to the result list
        result.append(digits[diff])

    # If there is still a borrow left, it means the result is negative.
    if borrow:
        return base_n_subtract(num2, num1, base)
    return ''.join(result[::-1])


# print count of numbers in a number system with base N
for i in range(0, count+1):
    print(((base10_to_baseN(i, base))), end=" ")
print()

# adding two numbers in base
num1 = base10_to_baseN(num1,base)
num2 =  base10_to_baseN(num2,base)
print(num1)
print(num2)
print(addition(num1,num2,base))
#
# # multiplication of two numbers in base
# multiplication_val = multiplication(num1,num2_base10, base)
# print(multiplication_val)
#
# #base 10 Conversion
# print(base10Converter(int(multiplication_val),base))
#
# #base N to base M conversion
# print(base_n_converter(int(multiplication_val),base,new_base))
#
# print(base_n_subtract(str(num1),str(num2),base))
