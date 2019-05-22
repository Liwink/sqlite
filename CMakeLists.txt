project(sqlite)
cmake_minimum_required(VERSION 3.12)

include_directories(${CMAKE_SOURCE_DIR}/src)
# add_library(sqlite3 STATIC src/*.c, src/*.h)
# add_library(sqlite3 STATIC ext/rtree/rtree.c ext/rtree/rtree.h src/vtab.c src/loadext.c)
add_library(sqlite3 STATIC ext/rtree/rtree.c ext/rtree/rtree.h src/vtab.c src/vdbe.c src/vdbeapi.c src/where.c
        src/select.c src/vdbeblob.c)

