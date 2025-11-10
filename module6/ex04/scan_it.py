#!/usr/bin/env python3

import re
import sys

args = sys.argv[1:];
if len(args) < 2:
    print("none");
else:
    result_re = re.findall(fr"{args[0]}", args[1]);
    result_num = len(result_re);
    if result_num == 0:
        print("none");
    else:
        print(result_num);