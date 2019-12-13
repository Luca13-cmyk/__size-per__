#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys


def show_size(target_def, type_def):
    if type_def == '-k':
        print(f"{round(os.path.getsize(target_def) / 1000, 5)} Kilobytes")
        return
    if type_def == '-m':
        print(f"{round(os.path.getsize(target_def) / 1_000_000, 5)} Megabytes")
        return
    if type_def == '-g':
        print(f"{round(os.path.getsize(target_def) / 1_000_000_000, 5)} Gigabytes")
        return
    if type_def == '-h' or type_def == '--help':
        print("USE -g to Gigabytes -> python3 __size-per__.py -g [TARGET]")
        print("USE -m to Megabytes -> python3 __size-per__.py -m [TARGET]")
        print("USE -k to Kilobytes -> python3 __size-per__.py -k [TARGET]")
        print("WARNING: only python 3.7+.")


try:
    type_ret = str(sys.argv[1])
    target_ret = str(sys.argv[2])

except IndexError:
    print("USE -g to Gigabytes -> python3 __size-per__.py -g [TARGET]")
    print("USE -m to Megabytes -> python3 __size-per__.py -m [TARGET]")
    print("USE -k to Kilobytes -> python3 __size-per__.py -k [TARGET]")
    print("WARNING: only python 3.7+.")
else:
    show_size(target_ret, type_ret)

