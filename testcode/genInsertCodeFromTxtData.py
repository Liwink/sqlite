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

  rc = sqlite3_open("newRtreeSmallRec50K.db", &db);
  if (rc) {
    fprintf(stderr, "Can't open database: %s", sqlite3_errmsg(db));
    sqlite3_close(db);
    return(1);
  }
  char *sql = "drop table if exists demo;"
  "CREATE VIRTUAL TABLE demo USING rtree(id, minX, maxX, minY, maxY);"
  "INSERT INTO demo VALUES "
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
f = open('../data/central_america_points_GEOMETRY.csv')

id = 1
list = []
for i in range(0, 50000):
    x_min = random.randint(-100000, 100000)
    x_len = random.randint(1, 3)

    y_min = random.randint(-100000, 100000)
    y_len = random.randint(1, 3)
    # list.append((str(id), str(x_min), str(x_min + x_len), str(y_min), str(y_min + y_len)))
    list.append(str((id, x_min, x_min + x_len, y_min, y_min + y_len)))
    id = id + 1

# with open('../insert_data_big.txt', 'w') as filehandle:
#     filehandle.write('INSERT INTO demo VALUES')
#     str = ''
#     str = str + ('%s ' % (','.join(item for item in data)))
#     filehandle.write(str)
#     filehandle.write(';')

with open('/Users/donghe/Desktop/SecondSemester/CS386D/insert_data_50K_test.c', 'w') as filehandle:
    str = ('%s ' % (','.join(item for item in list)))
    filehandle.write(code_start + '"' + str + ';"' + code_end)
    # filehandle.write("w")
filehandle.close()