#!/usr/bin/env python3

import sys

params = sys.argv[1:] #รับตั้งแต่ indx1 ->indx last

if len(params) < 2:
    print("none")
else:
    for param in reversed(params):
        print(param)