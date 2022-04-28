def key_value(dictA):
    b = []
    c = []
    for i in dictA:
        b.append(i)
        c.append(dictA[i])
    return b, c 

list_key, list_val = key_value({'name' : 'John', 'age' : 32}) 
print(list_key)
print(list_val) 