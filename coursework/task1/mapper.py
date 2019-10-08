#!/usr/bin/python2.7

import sys

DATA_DELIMITER = '\t'
LIST_DELIMITER = ","
OUTPUT_FORMAT = "%s|%s"
SKIP_VAL = "\\N"


def map_function(line):
    fields = line.strip().split(DATA_DELIMITER)         # separate input line
    runtime, genres = fields[7], fields[8]              # get runtime and list of genres
    if genres != SKIP_VAL and runtime != SKIP_VAL:      # if both exist
        for g in genres.strip().split(LIST_DELIMITER):  # iterate and yield (k,v) = (genre, runtime)
            yield g, runtime


for line in sys.stdin:
    for key, value in map_function(line):
        print(OUTPUT_FORMAT % (key, value))
