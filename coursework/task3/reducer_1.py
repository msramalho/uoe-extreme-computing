#!/usr/bin/python2.7

import sys
from collections import namedtuple


class Movie:
    def __init__(self, id=None, title=None, genres=None, decade=None, rating=None):
        self.id = id
        self.title = title
        self.genres = genres
        self.decade = decade
        self.rating = rating

    def update(self, fields):
        self.id = fields[0]
        if len(fields) == 2:            # id|rating
            self.rating = fields[1]
        else:                           # id|decade|genres|title
            self.decade = fields[1]
            self.genres = fields[2]
            self.title = fields[3]

    def _print(self):
        # print if info from both ratings and basics was found
        if self.rating and self.decade:
            # output var is used to avoid repeating the format operation unnecessarily
            # the movie id is not passed as it would be irrelevant info
            output = "%s|%%s|%s|%s" % (self.decade, self.title, self.rating)  # notice the %%
            for genre in self.genres.split(","):
                print(output % genre)


m = Movie()
for line in sys.stdin:
    fields = line.strip().split("|")
    if fields[0] == m.id:  # same key
        m.update(fields)
    else:
        m._print()
        m = Movie()
        m.update(fields)
else:  # finally, print the last movie
    m._print()
