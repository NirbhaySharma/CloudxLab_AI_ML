num = 10
series = []

def generate_series(num):
    global series
    for i in range(0, num):
        if i == 0 or i == 1:
            series.append(1)
        else :
            series.append(series[i-1] + series[i-2])

generate_series(num)
print(series)
