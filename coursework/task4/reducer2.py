#!/usr/bin/python2.7

import sys

counter = 0
for line in sys.stdin:
    if counter >= 10: break
    print(line.strip())
    counter+=1
