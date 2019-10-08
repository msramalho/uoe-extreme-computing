#!/usr/bin/python2.7

import sys
from collections import namedtuple

DATA_DELIMITER = '\t'
OUTPUT_FORMAT = "%s|%s"
SKIP_VAL = "\\N"


def validate(named_tuple, properties):
    # for each of the provided properties, guarantee that none is SKIP_VAL
    return not any(getattr(named_tuple, p) == SKIP_VAL for p in properties)


def _print(output):
    # print if output is valid
    if output != None: print(output)


# basics.tsv related code
Movie = namedtuple('Movie', 'id type title original adult release end duration genres')
def map_basics(fields):
    # basics.tsv input should send id|decade|genres|title
    # could emit one tuple per genre, but that would be a waste of resources
    # since that is only needed for the next MapReduce Job
    m = Movie(*fields)
    if validate(m, ["type", "title", "release", "genres"]) and m.type == "movie":
        release = int(m.release)
        if 1900 <= release and release <= 1999:                             # only 20th century movies
            return "%s|%s|%s|%s" % (m.id, m.release[2], m.genres, m.title)  # release[2] yields decade


# ratings.tsv related code
def map_ratings(fields):
    # in case this is a line from the ratings.tsv file
    # no filtering required, just output id|rating
    return "%s|%s" % (fields[0], fields[1])


# main code
def map_function(line):
    # split line and return according to input type (basics, ratings)
    fields = line.strip().split(DATA_DELIMITER)
    return map_basics(fields) if len(fields) == 9 else map_ratings(fields)


for line in sys.stdin:
    _print(map_function(line))
