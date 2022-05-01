def key_and_value(dictA):
    key = dictA.keys()
    value = dictA.values()
    return key, value
key, value = key_and_value({'a' : 1, 'B' : 2, 'C' : 3})
print(key)
print(value)    