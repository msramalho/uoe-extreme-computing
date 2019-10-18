#!/usr/bin/python2.7

"""
Output: 
    id|A[Title]         title.basics.tsv
    id|B                title.ratings.tsv
"""

import sys
from collections import namedtuple

DATA_DELIMITER = '\t'
SKIP_VAL = "\\N"

Movie = namedtuple('Movie', 'id type title original adult release end duration genres')


def validate(named_tuple, properties):
    # for each of the provided properties, guarantee that none is SKIP_VAL
    return all(getattr(named_tuple, p) != SKIP_VAL for p in properties)


def _print(output):
    # print if output is valid
    if output != None: print(output)


def map_basics(fields):
    # in case this is a line from the title.basics.tsv file
    # it should be filtered on release year
    # the output starts with "B" so that the reducer can differentiate
    m = Movie(*fields)                                      # cast to namedtuple
    if m.type == "movie" and validate(m, ["release", "title"]):
        release = int(m.release)
        if 1990 <= release and release <= 2018:
            return "%s|A%s" % (m.id, m.title)


def map_ratings(fields):
    # in case this is a line from the ratings.tsv file
    # it should be filtered on >=50k votes and rating >=7.5
    # the output starts with "R" so that the reducer can differentiate
    rating, votes = float(fields[1]), int(fields[2])
    if rating >= 7.5 and votes >= 50000:
        return "%s|B" % fields[0]


def map_function(line):
    # split line and return according to input type (basics, ratings)
    fields = line.strip().split(DATA_DELIMITER)
    return map_basics(fields) if len(fields) == 9 else map_ratings(fields)


for line in sys.stdin:
    _print(map_function(line))
