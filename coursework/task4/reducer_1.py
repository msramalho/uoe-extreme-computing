#!/usr/bin/python2.7

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
        if len(fields) == 3:  # crew file
            self.writer = fields[2]
        else:  # names file len = 4
            self.known_for = fields[2]
            self.name = fields[3]

    def _print(self):
        if self.name and self.writer == self.known_for:
            print("%s|%s" % (self.votes, self.name))
            self.name = None


m = Movie()
for line in sys.stdin:
    fields = line.strip().split("|")
    if fields[0] == m.id:  # same movie
        m.update(fields)
        # TODO: wait for reply on non-duplicates, otherwise print should be controlled with is_printed
        m._print()
    elif fields[1] == "A":  # skip if A is not seen before changing key
        m._print()
        m = Movie(id=fields[0], votes=fields[2])
else:  # finally, print the last movie
    m._print()
