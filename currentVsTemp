


'''
Reference : https://www.researchgate.net/figure/Graph-between-Temperature-Vs
-Voltage-V-Current-A_fig7_321331172

Considering the above graph we are able to deduce the pattern in graph to be
somewhere near a linear.

Hence considering the data points and values. The approach is to find the
average linear curve of the temp and find the local deviation of that
particular value and the nearby values and then calculate the value
accordingly
'''

temprature_points = [20, 30, 40 , 50, 60, 70, 80, 90, 100,110]
current_points = [15,19,23,60,82,96,104,142,192,234]
average_deviation = 0
mean_current_points = []
check_temp = 41

for index, value in enumerate(current_points):
    if index == 0:
        continue
    average_deviation += (value - current_points[index-1])

average_deviation = average_deviation/ (len(current_points)-1)

for index, value in enumerate(current_points):
    if index == 0:
        mean_current_points.append((current_points[index],1))
        continue
    val = (current_points[0] + (average_deviation *
                                index))
    mean_current_points.append((val,current_points[index]/val))
print(average_deviation)
print(mean_current_points)


def low_high_temp(temp):
    for i,v in enumerate(temprature_points):
        if v <= temp <= temprature_points[i+1]:
            return (i,v,temprature_points[i+1])


def deviation_unit(temp, low, high, low_ind):
    weight = ((temp - low) / (high - low))
    value = ((weight * mean_current_points[(low_ind + 1)][1] *
             mean_current_points[(low_ind + 1)][0])) + (( (1-weight) *
                                                        mean_current_points[(low_ind)][1] *
                                                       mean_current_points[(low_ind)][0]))
    return value

def find_current(temp):
    if (20 > temp) or (temp > 110):
        return -1
    low_ind,low,high = low_high_temp(temp)
    return deviation_unit(temp, low, high,low_ind)

print(find_current(check_temp))
