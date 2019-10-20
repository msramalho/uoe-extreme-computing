#!/usr/bin/python2.7

"""
Output:
writerId|movieIds|votes
"""

import sys
sys.path.append('./')
from movie import Movie

m = Movie()
for line in sys.stdin:
    m.parse_line(line)
else:
    m._print()
