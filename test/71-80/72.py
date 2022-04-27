n = int(input('= '))
list1 = []
for i in range(n):
      float1 = float(input('= '))
      list1.append(float1)
mean_list = sum(list1) / len(list1)
var_list = 0
for x in list1:
    var_list += (x - mean_list) ** 2
var_list /= len(list1)
dict1 = {}
dict1['mean'] = mean_list
dict1['variance'] = var_list
print(dict1)


