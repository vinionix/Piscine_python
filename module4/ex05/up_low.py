#!/usr/bin/env python3

receiver = input("");
receiver2 = "";
i = 0;
for i in receiver:
    if i.isupper():
        receiver2 += i.lower();
    elif i.islower():
        receiver2 += i.upper();
if receiver2 != "":
    print(receiver2);
else:
    print(receiver);