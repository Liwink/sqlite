code_start = '''
#include <stdio.h>
#include <time.h>
#include "sqlite3.h"

// gcc script.c -DSQLITE_ENABLE_RTREE sqlite3.h sqlite3.c
char* getDateTime() {
  static char nowtime[20];
  time_t rawtime;
  struct tm *ltime;
  time(&rawtime);
  ltime = localtime(&rawtime);
  strftime(nowtime, 20, "%Y-%m-%d %H:%M:%S", ltime);
  return nowtime;
}

int main(int argc, char **argv) {
  sqlite3 *db;
  int rc;
  char *err_msg = 0;

  rc = sqlite3_open("central_america_points_GEOMETRY.db", &db);
  if (rc) {
    fprintf(stderr, "Can't open database: %s", sqlite3_errmsg(db));
    sqlite3_close(db);
    return(1);
  }
  char *sql = 
'''

code_end = '''
  ;

  time_t t;
    struct tm *timeinfo;  
  time(&t);
  timeinfo = localtime(&t);
  //char *startTimeStr = asctime(timeinfo);
  printf("start time = %s      ", asctime(timeinfo));

  time_t c_start;
  c_start = clock();    

  rc = sqlite3_exec(db, sql, 0, 0, &err_msg);

  time_t c_end;
  c_end = clock();

  time_t t1;
    struct tm *timeinfo1;  
  time(&t1);
  timeinfo1 = localtime(&t1);
  //char *endTimeStr = asctime(timeinfo1);
  printf("end time = %s        ", asctime(timeinfo1));

  if (rc) {
    fprintf(stderr, "SQL error: %s", err_msg);

    sqlite3_free(err_msg);
    sqlite3_close(db);

    return 1;
  }

  sqlite3_stmt *res;

  rc = sqlite3_prepare_v2(db, "select count(distinct(id)) from demo;", -1, &res, 0);

  if (rc != SQLITE_OK) {

    fprintf(stderr, "Failed to fetch data: %s     ", sqlite3_errmsg(db));
    sqlite3_close(db);

    return 1;
  }

  printf("Used time =: %f ms ",difftime(c_end,c_start) / 1000);

  sqlite3_close(db);

}
'''

import random


# id = 1
# list = []
# for i in range(0, 1000):
#     x_min = random.randint(-100000, 100000)
#     # x_len = random.randint(1, 3)
#
#     y_min = random.randint(-100000, 100000)
#     # y_len = random.randint(1, 3)
#     # list.append((str(id), str(x_min), str(x_min + x_len), str(y_min), str(y_min + y_len)))
#     list.append([id, x_min, x_min, y_min, y_min])
#     id = id + 1

# with open('../insert_data_big.txt', 'w') as filehandle:
#     filehandle.write('INSERT INTO demo VALUES')
#     str = ''
#     str = str + ('%s ' % (','.join(item for item in data)))
#     filehandle.write(str)
#     filehandle.write(';')

#f = open('../data/central_america_points_GEOMETRY.csv')

import re

f = open('../data/central_america_points_GEOMETRY.csv')
data_size = 1000

data = []
i = 0
for line in f:
    if i > data_size:
        break
    if i != 0:
        line = str(line.rstrip().split('\n'))
        nums = line.split(",")

        nums = line.split(',')
        data.append([i, (float)(nums[1]), (float)(nums[1]), (float)(nums[3]), (float)(nums[3])])
    i = i + 1

with open('/Users/donghe/Desktop/SecondSemester/CS386D/point_query_real_data_' + str(data_size/1000) + 'K.c', 'w') as filehandle:
    str = ''
    for item in data:
        str = str + ('SELECT * from demo where minX <= {} and maxX >= {} and minY <= {} and maxY >= {}; ').format(
            item[1], item[1], item[3], item[3])

    filehandle.write(code_start + '"' + str + '"' + code_end)

    # filehandle.write("w")
filehandle.close()