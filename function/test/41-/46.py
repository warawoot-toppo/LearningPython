def isTriangle(a, b, c):
    s_len = sorted([a, b, c])
    if s_len[0] + s_len[1] > s_len[2]:
        return True
    else:
        return False

print(isTriangle(5, 3, 4))            