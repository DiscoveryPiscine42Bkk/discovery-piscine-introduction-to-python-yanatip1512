#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    for arg in reversed(args):
        print(arg)