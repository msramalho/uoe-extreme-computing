#!/usr/bin/python2.7

"""
Output:
writerId|movieIds|votes
"""

import sys
sys.path.append('./')
from movie import Movie

class MovieCombiner(Movie):
    def _print_combiner(self):
        if self.votes: # re-emit ratings file   
            print("%s|%s" % (self.id, self.votes))
        elif self.writers:
            print("%s|%s" % (self.id, self.writers))

m = MovieCombiner()
for line in sys.stdin:
    m.parse_line(line)
else:
    m._print()
    m._print_combiner()
