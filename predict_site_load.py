data = [(0,10),(1,15),(2,30)]

def fit(data):
    vals = []
    for i in data:
        vals.append((i[0] * i[0],i[0],i[1]))
    print(vals)
    a = ((((vals[1][2]- vals[0][2])* (vals[2][1] - vals[1][1])) -
         ((vals[2][2]- vals[1][2])* (vals[1][1] - vals[0][1]))) /
         ((( vals[1][0] - vals[0][0])*(vals[2][1] - vals[1][1]))
         -((vals[2][0] - vals[1][0])*(vals[1][1] - vals[0][1]))))
    b = ((vals[1][2] - vals[0][2]) - (a * (vals[1][0]-vals[0][0]))
         /(vals[1][1]-vals[0][1]))
    c = vals[2][2] - (b* vals[2][1]) - (a * vals[2][0])
    return (a,b,c)

model = fit(data)
def cal_load(t,model):
    load = (model[0] * t *t) + (model[1] * t) + model[2]
    return load

print(cal_load(3,model))
