#!/usr/bin/env python3

class table:
    def __init__(tab, number):
        tab.num = number;
    def print_table(number):
        print(f"Table of {tab.num}:", end=' ');
        number_temp = tab.num;
        for i in range(11):
            result = i * number_temp;
            print(result, end=' ');
        if (tab.num != 10):
            print();
for i in range(11):
    tab = table(i);
    tab.print_table();