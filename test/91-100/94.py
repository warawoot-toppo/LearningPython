list1 = [1, 3, 7, 9, 2, 7 ,5, 1, 8]
sorted_list = sorted(list1)
if len(sorted_list) % 2 == 1:
    posi = int((len(sorted_list) - 1) / 2)
    median = sorted_list[posi]
else:
    posi1 = int(len(sorted_list) / 2 - 1)
    posi2 = int(len(sorted_list) / 2)
    median = (sorted_list[posi1] + sorted_list[posi2]) / 2
print(median)     