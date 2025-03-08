cmake_minimum_required(VERSION 3.27)
project(the1 C)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c90 -pedantic-errors -ansi ")

add_executable(the1 the1.c)
