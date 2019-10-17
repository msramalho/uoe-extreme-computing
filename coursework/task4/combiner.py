#!/usr/bin/python2.7

"""
Input (sorted on first 3 columns)       FROM
movieId|A|votes                         name.basics.tsv
movieId|B|personId|Name                 name.basics.tsv
movieId|B|personId                      title.crew.tsv

Output:
votes|Name                              for writers AND knownFor in the same movieId

Repeats the following output:
movieId|A|votes                         name.basics.tsv

Repeats the following output if not able to reduce in combiner:
movieId|B|personId|Name                 name.basics.tsv
movieId|B|personId                      title.crew.tsv
"""

import sys
from collections import namedtuple
sys.path.append('./')
from movie import Movie


class MovieCombiner(Movie):
    def _print_combiner(self, printed_info, change_movie):
        if change_movie and self.id: # re-emit A line after changing movie
            print("%s|A|%s" % (self.id, self.votes))
        if not printed_info and self.new_writer:
            self.new_writer = False 
            if self.name:   # only found name.basics.tsv input, re-emit
                print("%s|B|%s|%s" % (self.id, self.known_for, self.name))
                # self.name = None
            else:           # only found title.crew.tsv, re-emit
                print("%s|B|%s" % (self.id, self.writer))
                # self.writer = None

m = MovieCombiner()
for line in sys.stdin:
    m.parse_line(line)
else:
    m._print()
