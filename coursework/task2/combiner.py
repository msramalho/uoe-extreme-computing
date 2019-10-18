#!/usr/bin/python2.7

"""
Output reduced:
Title

Output not-reduced (re-emitted):
id|A[Title]         title.basics.tsv
id|B                title.ratings.tsv
"""

import sys
sys.path.append('./')
from movie import Movie


class MovieCombiner(Movie):
    def _print_combiner(self):
        if self.id:         # print as mapper would
            if self.title:  # aka filter1
                print("%s|A%s" % (self.id, self.title))
            else:           # aka filter 2
                print("%s|B" % self.id)


movie = MovieCombiner()
for line in sys.stdin:
    movie.parse_line(line)
else:
    movie._print()
