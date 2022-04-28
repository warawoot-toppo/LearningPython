def string1(a, b):
    str_1 = ''
    for i in range(len(a)):
        str_1 += (a[i] + b[i])
    return str_1

mix = string1(['ห', 'า', 'ุ'], ['ม', 'น', 'ด'])
print(mix)