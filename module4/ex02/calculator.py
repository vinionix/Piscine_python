#!/usr/bin/env python3

try:
    number1 = int(input("Give me the first number: "));
    number2 = int(input("Give me the second number: "));
    print("Thank you!");
    print(number1, '+', number2, '=', int(number1 + number2));
    print(number1, '-', number2, '=', int(number1 - number2));
    print(number1, '/', number2, '=', int(number1 / number2));
    print(number1, '*', number2, '=', int(number1 * number2));
except:
    print(end="");