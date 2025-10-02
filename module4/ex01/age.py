#!/usr/bin/env python3

try:
    age = int(input("Please tell me your age: "));
    print(f"You are currently {age} years old.");
    i = 10;
    while i <= 30:
        future_age = i + age;
        print(f"In {i} years, you'll be {future_age} years old.");
        i+=10;
except:
    print(end='');