#!/usr/bin/python2.7

"""
Output:                 Input:
movieId|votes           title.ratings.tsv
movieId|writerIds       title.crew.tsv
"""

import sys
from collections import namedtuple

DATA_DELIMITER = '\t'
SKIP_VAL = "\\N"


def validate(named_tuple, properties):
    # for each of the provided properties, guarantee that none is SKIP_VAL
    return all(getattr(named_tuple, p) != SKIP_VAL for p in properties)


def _print(output):
    # print if output is valid
    if output != None: print(output)


# ratings.tsv related code
def map_ratings(fields):
    return "%s|%s" % (fields[0], fields[2])


# title.crew.tsv related code
def map_crew(fields):
    Crew = namedtuple('Crew', 'movie_id directors writers')
    c = Crew(*fields)
    if validate(c, ["writers"]):
        return "%s|%s" % (c.movie_id, c.writers)


def map_function(line):
    fields = line.strip().split(DATA_DELIMITER)
    if unicode(fields[2]).isnumeric(): return map_ratings(fields)
    else: return map_crew(fields)


for line in sys.stdin:
    _print(map_function(line))
