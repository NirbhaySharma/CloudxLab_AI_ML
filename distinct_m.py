def distinct_m1(factors):
    for i in range(len(factors)-1,0,-1):
        if(factors[i-1] == factors[i]):
            del factors[i]
    return factors

print(distinct_m1([1,1,1,1,1,2,2,3,4,5,6,7,7,7,8,8]))
