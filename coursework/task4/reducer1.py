#!/usr/bin/python2.7

"""
Input (sorted on first 2 columns):
movieId|A|votes             # from name.basics.tsv
movieId|B|personId|Name     # from name.basics.tsv
movieId|B|personId          # from title.crew.tsv

Output:
votes|Name                  # for writers AND knownFor in the same movieId
"""

import sys
from collections import namedtuple


class Movie:
    def __init__(self, id=None, votes=None, writer=None, known_for=None, name=None):
        self.id = id
        self.votes = votes
        self.writer = writer
        self.known_for = known_for
        self.name = name

    def update(self, fields):
        if len(fields) == 3:            # crew file
            self.writer = fields[2]
        else:                           # names file, len=4
            self.known_for = fields[2]
            self.name = fields[3]

    def _print(self):
        if self.name and self.writer == self.known_for:
            print("%s|%s" % (self.votes, self.name))
            self.name = None


m = Movie()
for line in sys.stdin:
    # print("-----------" + line.strip())
    fields = line.strip().strip("|").split("|")
    if fields[0] == m.id:   # same movie
        m.update(fields)
        m._print()
    elif fields[1] == "A":  # skip if A is not seen before changing key
        m._print()          # print the previous TODO: is this necessary?
        m = Movie(id=fields[0], votes=fields[2])
else:  # finally, print the last movie
    m._print()
