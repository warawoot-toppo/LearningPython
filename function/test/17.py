def remove_str(str1):
    a = '!@#\$%,'
    for i in a:
        
        str1 = str1.replace(i, '')
    return str1    

str1 = 't!o@p#p$o'    
print(remove_str(str1))