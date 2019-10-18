#!/usr/bin/python2.7

import sys
sys.path.append('./')
from movie2 import Movie


class MovieCombiner(Movie):
    def _print(self):
        # combiner version of _print has to re-emit the title as this may not be the highest and only the reducer will be able to tell
        if self.title:
            print("%s|%s|%s|%s" % (self.decade, self.genre, self.title, self.rating))

m = MovieCombiner()
for line in sys.stdin:
    m.parse_line(line)
else:
    m._print()
