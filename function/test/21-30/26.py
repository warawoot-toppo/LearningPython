def per_interest(pv, fv, n):
    r = ((fv / pv) ** (1 / n) - 1) * 100
    return r

print(per_interest(1000, 7000, 6))