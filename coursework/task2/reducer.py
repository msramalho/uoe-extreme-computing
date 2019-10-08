#!/usr/bin/python2.7

import sys

# global variables
OUTPUT_FORMAT = "%s"  # [title:str]


class Movie:
    def __init__(self, id=None, filter1=False, filter2=False, title=None):
        self.id = id
        self.filter1 = filter1
        self.filter2 = filter2
        self.title = title

    def update_filter(self, value):
        # update the filter according to the received key
        if value == "R":            # ratings.tsv mapper
            self.filter2 = True
        else:                       # basics.tsv mapper
            self.filter1 = True
            self.title = value[1:]

    def _print(self):
        # print title if valid and all filters have been checked
        if self.id and self.filter1 and self.filter2:
            print(self.title)


movie = Movie()
for line in sys.stdin:
    # print(line)
    # continue
    id, value = line.strip().split("|", 1)
    print(id + "|" + value)
    continue

    if movie.id == id:  # same key
        movie.update_filter(value)
    else:
        movie._print()
        movie = Movie(id)
        movie.update_filter(value)
else:  # finally, print the last movie
    movie._print()
