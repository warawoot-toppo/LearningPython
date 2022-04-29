def word(str1, k):
    w = (str1 + '-')
    wk = w * k
    return wk[:-1]

print(word('one', 3))