data = {'Brazil' : 35000, 'China' : 24000, 'Germany' : 42000, 'Japan' : 53000, 'Sweden' : 17000}
list1 = list(data.values())
sorted_list = sorted(list1)
if len(sorted_list) % 2 == 1:
    posi = int((len(sorted_list) - 1) / 2)
    median = sorted_list[posi]
else:
    posi1 = int(len(sorted_list) / 2 - 1)
    posi2 = int(len(sorted_list) / 2)
    median = (sorted_list[posi1] + sorted_list[posi2]) / 2
print(median)        