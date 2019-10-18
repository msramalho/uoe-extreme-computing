#!/usr/bin/python2.7

import sys
sys.path.append('./')
from movie2 import Movie

m = Movie()
for line in sys.stdin:
    m.parse_line(line)
else:
    m._print()
