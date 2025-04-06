
devident = 4
devisor = 0

def cust_devision(devident,devisor):
    if devisor == 0:
        return 'infinity'
    devident_neg = False
    devisor_neg = False
    if(devident < 0):
        devident_neg=True
    if(devisor < 0):
        devisor_neg=True
    devident = abs(devident)
    devisor = abs(devisor)
    if devident < devisor:
        return (0,devident)
    count = 0
    while True:
        count += 1
        devident -= devisor
        if(devident < devisor):
            if devident_neg and devisor_neg:
                return (count, devident*-1)
            elif devident_neg and not(devisor_neg):
                return ((count +1)*-1, (devisor - devident))
            elif not(devident_neg) and devisor_neg:
                return ((count +1)*-1, (devisor - devident)*-1)
            else: return (count, devident)

print(cust_devision(16,5))
print(cust_devision(-16,-5))
print(cust_devision(-16,5))
print(cust_devision(16,-5))

