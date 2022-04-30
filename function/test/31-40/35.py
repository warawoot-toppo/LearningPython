def to_hexadecimal(x):
    converter = {0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6',
    7 : '7', 8 : '8', 9 : '9', 10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
    import math
    n_bit = math.floor(math.log(x,16))
    hexa = ''
    for bit in range(n_bit, -1, -1):
        s = x // int(16**bit)
        hexa += converter[s]
        x -= s * 16 ** bit
    return hexa

print(to_hexadecimal(318))
