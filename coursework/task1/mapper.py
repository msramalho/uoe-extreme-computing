#!/usr/bin/python2.7

import sys
from collections import namedtuple

DATA_DELIMITER = '\t'
LIST_DELIMITER = ","
OUTPUT_FORMAT = "%s|%s"
SKIP_VAL = "\\N"


def validate(named_tuple, properties):
    # for each of the provided properties, guarantee that none is SKIP_VAL
    return not any(getattr(named_tuple, p) == SKIP_VAL for p in properties)


Movie = namedtuple('Movie', 'id type title original adult release end duration genres')


def map_function(line):
    fields = line.strip().split(DATA_DELIMITER)             # separate input line
    m = Movie(*fields)                                      # cast to namedtuple
    if validate(m, ["duration", "genres"]):                 # if both exist
        for g in m.genres.strip().split(LIST_DELIMITER):    # iterate and yield (k,v) = (genre, runtime)
            yield g, m.duration


for line in sys.stdin:
    for key, value in map_function(line):
        print(OUTPUT_FORMAT % (key, value))
