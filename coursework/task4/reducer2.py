#!/usr/bin/python2.7

import sys
sys.path.append('./')
from writer import Writer

w = Writer()
for line in sys.stdin: w.parse_line(line)
w._print_result()
