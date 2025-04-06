from math import sqrt

def find_factors(num):
    factors = []
    while True:
        found = False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                factors.append(i)
                num = num//i
                found = True
                break
        if not found:
            factors.append(num)
            break
    return factors

def find_factors_slow(num):
    for i in range(2, num):
        if num % i == 0:
            new_num = num//i
            new_factors = find_factors_slow(new_num)
            return [i] + new_factors
    return [num]

print(find_factors(27))
print(find_factors_slow(27))
