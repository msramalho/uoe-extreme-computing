#!/usr/bin/python2.7

import sys
from collections import namedtuple


class Movie:
    def __init__(self, decade=None, genre=None, title=None, rating=-1):
        self.decade = decade
        self.genre = genre
        self.title = title
        self.rating = rating

    def update(self, fields):
        # assert self.is_same(fields), "must have same decade,genre tuple"
        self.decade = fields[0]
        self.genre = fields[1]
        new_rating = float(fields[3])
        if self.rating < new_rating:    # if the new film has higher rating
            self.rating = new_rating    # update the max rating
            self.title = fields[2]      # and the corresponding title

    def is_same(self, fields):
        return self.decade == fields[0] and self.genre == fields[1]

    def _print(self):
        # print result if video info is present
        if self.title:
            print("%s|%s|%s" % (self.decade, self.genre, self.title))


m = Movie()
for line in sys.stdin:
    fields = line.strip().split("|")
    if m.is_same(fields):  # same decade and genre
        m.update(fields)
    else:
        m._print()
        m = Movie()
        m.update(fields)
else:
    m._print()
