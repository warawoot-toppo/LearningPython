def interest(pv, r, n):
    fv = pv * (1 + r / 100) ** n
    return ('%.3f' %fv)

print(interest(5000, 15, 3))
