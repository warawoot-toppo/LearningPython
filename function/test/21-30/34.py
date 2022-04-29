def to_binary(x):
    import math
    n_bit = math.floor(math.log(x, 2))
    binary = ''
    for bit in range(n_bit, -1, -1):
        s = x // int(2 ** bit)
        binary += str(s)
        x -= s * 2 ** bit
    return binary

print(to_binary(5640))