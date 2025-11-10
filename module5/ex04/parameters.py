#!/usr/bin/env python3

import sys

args = sys.argv[1:];
x = 0;
while x < len(args):
    x+=1;
if x == 0:
    print("Number of parameters: 0.");
else:
    print(f"Number of parameters: {x}");
