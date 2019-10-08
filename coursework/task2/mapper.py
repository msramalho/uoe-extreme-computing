#!/usr/bin/python2.7

import sys

DATA_DELIMITER = '\t'
OUTPUT_FORMAT = "%s|%s"
SKIP_VAL = "\\N"


def map_basics(fields):
    # in case this is a line from the basics.tsv file
    # it should be filtered on release year
    # the output starts with "B" so that the reducer can differentiate
    title_type, title, release = fields[1], fields[2], fields[5]
    # if order is not random :-)
    if title_type == "movie" and release != SKIP_VAL and title != SKIP_VAL:
        release = int(release)
        if 1990 <= release and release <= 2018:
            return fields[0], "B" + title
    return False, None


def map_ratings(fields):
    # in case this is a line from the ratings.tsv file
    # it should be filtered on >=50k votes and rating >=7.5
    # the output starts with "R" so that the reducer can differentiate
    rating, votes = float(fields[1]), int(fields[2])
    if rating >= 7.5 and votes >= 50000: return fields[0], "R"
    return False, None


def map_function(line):
    # split line and return according to input type (basics, ratings)
    fields = line.strip().split(DATA_DELIMITER)
    yield map_basics(fields) if len(fields) == 9 else map_ratings(fields)


for line in sys.stdin:
    for key, value in map_function(line):
        if key != False:  # mappers will return False if invalid
            print(OUTPUT_FORMAT % (key, value))
