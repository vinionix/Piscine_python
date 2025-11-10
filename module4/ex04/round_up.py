#!/usr/bin/env python3

try :
    number = float(input("Give me a number: "));
    if number % 1 != 0:
        number += 1;
    number2 = int(number);
    print(number2);
except:
    print(end="");