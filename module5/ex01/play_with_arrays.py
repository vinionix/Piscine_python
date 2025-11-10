#!/usr/bin/env python3

try:
    enter = input("Insert numbers separated by space: ");
    my_array = [int(x) for x in enter.split()]
except:
    print("Input error");
    exit();
array2 = [i + 2 for i in my_array];

print(f"Original array: {my_array}")
print(f"New array {array2}");
