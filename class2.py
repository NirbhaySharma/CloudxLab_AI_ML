#finding the number digits needed to type a number in base B
import math

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
    return ((is_on_line(fx1,fx2,px1) and is_on_line(fy1,fy2,py1)) or (
            (is_on_line(fx1,fx2,px2) and is_on_line(fy1,fy2,py2)) ))

def find_required_digits(num,base):
    digit = 1
    while True:
        if(base**digit > num):
            return digit
        digit +=1


def find_pgt_len( point1, point2):
    val = 0
    for index in range(len(point1)):
        val += (point1[index] - point2[index]) ** 2
    return math.sqrt(val)


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
        temp = mid**power
        if num == temp:
            return mid
        elif num < temp and (temp - num) > 0.00001:
            high = mid
        elif num > temp and (num - temp) > 0.00001:
            low = mid
        else: return mid



print(is_on_line(2,1,1.5))
print(are_overlapping_lines(-1,-2,-1.5,1))
print(find_required_digits(num,base))
print(find_log10_value(1050))
print(find_rt(2,2))
print(find_cube(3))
print(are_overlapping_rect(1,2,3,4,3,4,5,6))
print(find_pgt_len((0,0,0),(3,4,3.33333334)))
