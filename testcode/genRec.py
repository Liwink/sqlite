import random

id = 1
list = []
for i in range(0, 100000):
    x_min = random.randint(-10000, 10000)
    x_len = random.randint(1, 5)

    y_min = random.randint(-10000, 10000)
    y_len = random.randint(1, 5)
    # list.append((str(id), str(x_min), str(x_min + x_len), str(y_min), str(y_min + y_len)))
    list.append(str((id, x_min, x_min + x_len, y_min, y_min + y_len)))
    id = id + 1

with open('big_data_set.txt', 'w') as filehandle:
    filehandle.write('INSERT INTO demo VALUES')
    str = ''
    str = str + ('%s ' % (','.join(listitem for listitem in list)))
    filehandle.write(str)
    filehandle.write(';')
