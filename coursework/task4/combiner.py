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
sys.path.append('./')
from movie import Movie

class MovieCombiner(Movie):
    def _print_combiner_a(self):  # re-emit A line after changing movie, if not None
        if self.id:
            print("%s|A|%s" % (self.id, self.votes))

    def _print_combiner_b(self):
        if self.known_for:          # only found name.basics.tsv input, re-emit
            print("%s|B|%s|%s" % (self.id, self.known_for, self.name))
        elif self.writer:           # only found title.crew.tsv, re-emit
            print("%s|B|%s" % (self.id, self.writer))
    def _print_combiner_default(self, line):
        print(line.strip().strip("|"))
        self._print_combiner_a()
        self.__init__(id=self.id, votes=self.votes)

m = MovieCombiner()
for line in sys.stdin:
    m.parse_line(line)
else:
    m._print()
    m._print_combiner_a()
