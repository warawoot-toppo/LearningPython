file_read = open('group_scores.txt')
file_write = open('22.3test.txt', 'w')

for i in file_read:
    d = 0
    t = i.split(' ')
    for h in t:
        r = int(h)
        d += r
    n = d / len(t)
    file_write.write(str(n) + '\n')
   
      

file_write.close()
file_read.close()