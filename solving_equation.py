import numpy as np

# Define the systems of equations
equs_1 = np.array([[3, 6, 2], [4, 9, 7], [5, 10, 1]])
d_1 = np.array([18, 38, 22])


equs_3 = np.array([[7, 2, 1], [8, 5, 3], [6, 3, 4]])
d_3 = np.array([14, 27, 20])

# Solve for x, y, z for each system
solution_1 = np.linalg.solve(equs_1, d_1)
solution_3 = np.linalg.solve(equs_3, d_3)

# Print solutions
print("Solution for system 1 (x, y, z):", solution_1)
print("Solution for system 3 (x, y, z):", solution_3)

equs = [
    [3, 6, 2, 18],
    [4, 9, 7, 38],
    [5, 10, 1, 22]
]

equs1 = [
    [7, 2, 1, 14],
    [8, 5, 3, 27],
    [6, 3, 4, 20]
]

equs2 = [
    [2, 4, 5, 19],
    [3, 6, 1, 17],
    [1, 2, 3, 10]
]

def find_x(equs):
    temp2 = []
    for i in equs:
        if len(i) != (len(equs) + 1):
            return "invalid equations"
    if len(equs) == 1:
        return [equs[0][1]/equs[0][0]]
    for i,eq in enumerate(equs):
        if i == (len(equs) - 1):
            continue
        temp1 = []
        temp2.append(temp1)
        for m,val in enumerate(eq):
            if m == len(eq)- 2:
                continue
            temp1.append(((val * equs[i+1][len(eq)- 2]) - (equs[i+1][m] *
                                                           eq[len(eq)- 2])))
    return find_x(temp2)

def solve_eq(equs):
    try:
        final_model = []
        tem = equs
        for i in range(0, len(equs)):
            x = find_x(tem)
            del tem[-1]
            final_model.append(x[0])
            for m, val in enumerate(tem):
                tem[m] = val[1:(len(val)-1)] + [(val[-1] - (x[0] * val[0]))]
        return final_model
    except:
        return "invalid equations: found divide by zero case"


print(solve_eq(equs))
print(solve_eq(equs1))
print(solve_eq(equs2))

