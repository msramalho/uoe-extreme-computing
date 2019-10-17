#!/usr/bin/python2.7

import sys

counter = 1
for line in sys.stdin:
    if counter > 10: continue
    print(line.strip().strip("|"))
    counter+=1
