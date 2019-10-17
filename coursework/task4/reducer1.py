#!/usr/bin/python2.7

"""
Input (sorted on first 3 columns)       FROM
movieId|A|votes                         name.basics.tsv
movieId|B|personId|Name                 name.basics.tsv
movieId|B|personId                      title.crew.tsv

Output:
votes|Name                              for writers AND knownFor in the same movieId
"""

import sys
from collections import namedtuple
sys.path.append('./')
from movie import Movie

m = Movie()
for line in sys.stdin:
    m.parse_line(line)
else:
    m._print()
