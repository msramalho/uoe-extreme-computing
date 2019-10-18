#!/usr/bin/python2.7

"""
Output:
decade|genre|title|rating
"""

import sys
sys.path.append('./')
from movie1 import Movie

m = Movie()
for line in sys.stdin:
    m.parse_line(line)
else:
    m._print()
