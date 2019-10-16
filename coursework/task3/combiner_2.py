#!/usr/bin/python2.7

import sys
from collections import namedtuple
sys.path.append('./')
from movie2 import Movie


class MovieCombiner(Movie):
    def _print(self):
        if self.title:
            print("%s|%s|%s|%s" % (self.decade, self.genre, self.title, self.rating))

m = MovieCombiner()
for line in sys.stdin:
    m.parse_line(line)
else:  # finally, print the last movie
    m._print()
