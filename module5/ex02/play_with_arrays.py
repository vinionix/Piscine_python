#!/usr/bin/env python3

try:
    enter = input("Insert numbers separated by space: ");
    my_array = [int(x) for x in enter.split()]
    print(my_array);
    for j in my_array[:]:
        if (j < 5):
            my_array.remove(j);
except:
    print("Input error");
    exit();
if (len(my_array) >= 1):
    my_array = [i + 2 for i in my_array];
    print(my_array);