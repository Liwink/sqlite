#include <stdio.h>
#include <sqlite3.h>

int main(int argc, char **argv) {
  sqlite3 *db;
  char *err_msg = 0;

  rc = sqlite3_open("test.db", &db);
  if (rc) {
    fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
    sqlite3_close(db);
    return(1);
  }

  char *sql = "drop table if exists rtree_test;"
    "CREATE VIRTUAL TABLE demo_index USING rtree(id, minX, maxX, minY, maxY);"
    "INSERT INTO demo_index VALUES(1, 1, 2, 3, 4);"
    "INSERT INTO demo_index VALUES(2, 0, 1, 1, 2);"
    "INSERT INTO demo_index VALUES(3, 2, 3, 0, 1);"
    "INSERT INTO demo_index VALUES(4, 7, 8, 5, 6);"
    "INSERT INTO demo_index VALUES(5, 6, 7, 3, 4);"
    "INSERT INTO demo_index VALUES(6, 9, 10, 1, 2);";

  rc = sqlite3_exec(db, sql, 0, 0, &err_msg);

  if (rc) {
    fprintf(stderr, "SQL error: %s\n", err_msg);

    sqlite3_free(err_msg);        
    sqlite3_close(db);

    return 1;
  }

  sqlite3_close(db);

}

