l1 = [1,2,3]
l2 = [2,4,6]
l3 = [9,8,5]

def xors(l1,l2,l3):
    resp = []
    for i in range(0, len(l1)):
        resp.append( (l1[i] ^ l2[i]) ^ l3[i])
    return resp

print(xors(l1,l2,l3))
