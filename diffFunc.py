def funct(x):
    return ((x**3))

print(funct(3))

def diff(f,x):
    deltas = [0.00001, 0.00002, 0.00000001, 0.1]
    ratios = []
    for i in range(0, len(deltas)):
        ratios.append((f(x+deltas[i]) - f(x) )/deltas[i])
    return ratios

print(diff(funct,2))
