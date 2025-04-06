list1 = '{{(){{[sbakfb[]](fanskgaskbkbaskb()),basbkks[{()}]nafkbk fsk}}}}'

def are_valid(check):
    lis =[]
    temp = None
    for i,x in enumerate(check):
        if x in "[{(":
            lis.append(x)
        if x in "]})":
            temp = lis.pop()
            if temp == "[" and x == "]":
                continue
            if temp == "{" and x == "}":
                continue
            if temp == "(" and x == ")":
                continue
            return "invalid"
    if len(lis) == 0:
        return "valid"
    else: return "invalid"

print(are_valid(list1))
