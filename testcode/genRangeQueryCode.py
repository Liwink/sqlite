import random

id = 1
list = []
for i in range(0, 1000):
    x_min = random.randint(-10000, 10000)
    x_len = random.randint(1, 20)

    # y_min = random.randint(-10000, 10000)
    # y_len = random.randint(1, 20)
    # list.append((str(id), str(x_min), str(x_min + x_len), str(y_min), str(y_min + y_len)))
    list.append([id, x_min, x_min + x_len])
    id = id + 1

with open('/Users/donghe/Desktop/SecondSemester/CS386D/rangeQuery1000.txt', 'w') as filehandle:
    str = ''
    for item in list:
        str = str + ('SELECT * from demo where minX >= {0} and maxX <= {1}; ').format(item[1], item[2])
    filehandle.write(str)