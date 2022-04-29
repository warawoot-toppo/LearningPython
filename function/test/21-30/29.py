def distance(x1,y1,x2,y2):
    
    distance1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
    return distance1

print(distance(3, 4, 6, 8))