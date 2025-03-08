polygon = [(0,0),(4,0),(5,3),(2,5),(-1,3)]
point= (5,5)

def is_on_line(point_1,point_2, check_point):
    if((point_1 <= check_point <= point_2) or (point_1 >= check_point >=
                                               point_2)):
        return True
    return False

def find_x(point_1,point_2,y):
    """
    delta y / delta x = delta y1/ delta x1
    :param point_1:
    :param point_2:
    :param y:
    :return:
    """
    delta_y = point_2[1] - point_1[1]
    delta_x = point_2[0] - point_1[0]
    delta_y1 = y - point_1[1]
    return (delta_x * delta_y1/delta_y) + point_1[0]

points = []

for i, v in enumerate(polygon):
    if i == 0:
        if(is_on_line(v[1],polygon[len(polygon) -1][1], point[1])):
            points.append((v,polygon[len(polygon) -1 ]))
    if i < (len(polygon)-1):
        if(is_on_line(v[1],polygon[i + 1][1], point[1])):
            points.append((v,polygon[i + 1]))

print(points)
def find_if_inside():
    if(len(points)== 2):
        print(find_x(points[0][0], points[0][1],point[1]))
        print(find_x(points[1][0], points[1][1],point[1]))
        return is_on_line(find_x(points[0][0], points[0][1],point[1]),find_x(
            points[1][0], points[1][1],point[1]), point[0])
    else:
        for i, val in enumerate(points):
            if(is_on_line(val[0][0],val[1][0],point[0])):
                return True
        return False


print(find_if_inside())
