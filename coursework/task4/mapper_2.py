#!/usr/bin/python2.7

import sys

for line in sys.stdin:
    print(line.strip()) # strip prevents empty lines


# TODO: mapper could remember the 10 most voted an pass only those larger than or equal to those
# could keep list with 11, update last and resort, to keep the 10best with O(1)