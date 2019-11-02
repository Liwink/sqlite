import random

id = 1
list = []
for i in range(0, 700):
    min_x = random.randint(-10000, 10000)
    max_x = random.randint(-10000, 10000)
    min_y = random.randint(-10000, 10000)
    max_y = random.randint(-10000, 10000)

    # list.append((str(id), str(x_min), str(x_min + x_len), str(y_min), str(y_min + y_len)))
    list.append([x])
    id = id + 1

with open('/Users/donghe/Desktop/SecondSemester/CS386D/pointQuery.txt', 'w') as filehandle:
    str = ''
    for item in list:
        str = str + ('SELECT * from demo where minX = {0} and maxX = {1} and minY = {2} and maxY = {3}; ').format(item[0], item[1], item[2], item[3])
    filehandle.write(str)