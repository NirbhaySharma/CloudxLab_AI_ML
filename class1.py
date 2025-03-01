import math
#Initializations
base = 6    # base value
count = 30  # Total numbers to be printed in your base system
new_base = 7  # New Base  one base to another base conversion
num1 = 5  # First number
multiplication_table_count = 8
digits = 4
number_to_represented_in_base = 1000
num2 = 4   # Second number
num2_base10 = num2
symbols= "0123456789abcdef"




#Functions
def base10_to_baseN(num: int,base: int) -> str:
    val = ''
    val = symbols[num % base] + val
    check = num // base
    if check < base:
        if(check == 0):
            return val
        val = symbols[check] + val
        return val
    else:
        recur = base10_to_baseN(check,base)
        val = recur  + val
        return val

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
     answer= '0'
     for i in range(0,num2_base10):
         answer = addition(answer,str(num1),base)
     return str(answer)

def base10Converter(num1 :str , base : int) -> int:
    sum = 0
    for i in range(1,len(num1) + 1):
        sum += int(symbols.index(num1[i *(-1)])) * base**(i-1)
    return sum


def base_n_converter(num1 : str, base : int,new_base : int):
    sum = 0
    for i in range(1,len(num1) + 1):
        sum += symbols.index(num1[i *(-1)]) * base**(i-1)
    return base10_to_baseN(sum,new_base)


def base_n_subtract(num1, num2, base):
    if base < 2 or base > 16:
        raise ValueError("Base must be between 2 and 16.")

    # Define the characters used in the given base
    digits = '0123456789abcdef'[:base]

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
print(f"printing {count} numbers in {base} base")
for i in range(0, count+1):
    print(((base10_to_baseN(i, base))), end=" ")
print()

# adding two numbers in base
numN1 = base10_to_baseN(num1,base)
numN2 =  base10_to_baseN(num2,base)
print(f"converting {num1} to base {base} : {numN1}")
print(f"converting {num2} to base {base} : {numN2}")

print(f"addition of {num1} and {num2} in base {base} :"
      f" {addition(numN1,numN2,base)}")
#
# # multiplication of two numbers in base
multiplication_val = multiplication(numN1,num2_base10, base)
print(f"Multiplication of {num1} and {num2} in base {base} :"
      f" {multiplication_val}")
#
# #base 10 Conversion
print(f"converting base 6 1 back to base 10 : {base10Converter((
    '1'),base)}")
print(f"converting base 6 10 back to base 10 : {base10Converter((
    '10'),base)}")
print(f"converting base 6 20 back to base 10 : {base10Converter((
    '20'),base)}")
print(f"converting base 6 30 back to base 10 : {base10Converter((
    '30'),base)}")
print(f"converting base 6 100 back to base 10 : {base10Converter((
    '100'),base)}")
#
# #base N to base M conversion
print(f"converting {multiplication_val} from base {base} to  base {new_base} :\
{base_n_converter(multiplication_val,base,new_base)}")

print(f"subtracting smaller number from bigger number ({num1},"
      f"{num2}) in base {base} : {base_n_subtract(\
    numN1,numN2,base)}")


for i in range(1,multiplication_table_count + 1):
    multiplication_val = multiplication(numN1,i, base)
    print(f"{num1} * {i} in base {base} :"
      f" {multiplication_val}")


print(f"How many numbers can be represented in base {base} ,{digits} digits "
      f"number: {(base**digits)}")

print(f"You need {(math.ceil(math.log(number_to_represented_in_base,base)))} "
      f"digits to represent {number_to_represented_in_base} in base {base}")

