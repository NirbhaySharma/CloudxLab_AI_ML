#finding the number digits needed to type a number in base B
num = 500
base = 7


def is_on_line(point_1,point_2, check_point):
    if((point_1 <= check_point <= point_2) or (point_1 >= check_point >=
                                               point_2)):
        return True
    return False

def are_overlapping_lines(point_1,point_2,point_3,point_4):
    return (is_on_line(point_1,point_2,point_3) or is_on_line(point_1,
                                                              point_2,point_4))


def are_overlapping_rect(fx1,fy1,fx2,fy2,px1,py1,px2,py2):
    return ((is_on_line(fx1,fx2,px1) and is_on_line(py1,py2,fy1)) or (
            is_on_line(px1,px2,fx1) and is_on_line(fy1,fy2,py1)) )

def find_required_digits(num,base):
    digit = 1
    while True:
        if(base**digit > num):
            return digit
        digit +=1


def find_log10_value(num):
    low = high = 0
    for i in range(0,10):
        if num <= 10**i:
            low = i - 1
            high = i
            if num == 10**i:
                return i
            break
    while True:
        mid = (high + low) / 2
        if num == 10**mid:
            return mid
        elif num < 10**mid and (10**mid - num) > 0.00001:
            high = mid
        elif num > 10**mid and (num - 10**mid) > 0.00001:
            low = mid
        else: return mid

def find_cube(num):
    return num**3

def find_rt(num,power):
    low = high = 0
    for i in range(0,num+1):
        if num <= i**power:
            low = i - 1
            high = i
            if num == i**power:
                return i
            break
    while True:
        mid = (high + low) / 2
        if num == mid**power:
            return mid
        elif num < mid**power and (mid**power - num) > 0.00001:
            high = mid
        elif num > mid**power and (num - mid**power) > 0.00001:
            low = mid
        else: return mid



print(is_on_line(2,1,1.5))
print(are_overlapping_lines(2,1,3,4))
print(find_required_digits(num,base))
print(find_log10_value(1050))
print(find_rt(64,3))
print(find_cube(3))
print(are_overlapping_rect(1,1,0,0,-2,-2,-1,-1))
