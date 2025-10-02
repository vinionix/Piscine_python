#!/usr/bin/env python3

try:
    number = int(input("Enter a number\n"));
    for i in range(10):
        result = i * number;
        print(i, "x", number, "=", result);
except ValueError:
    print("Error");