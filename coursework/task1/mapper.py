#!/usr/bin/python2.7

import sys

DATA_DELIMITER = '\t'
LIST_DELIMITER = ","
OUTPUT_FORMAT = "%s|%s"
SKIP_VAL = "\\N"


def map_function(line):
    fields = line.strip().split(DATA_DELIMITER)
    runtime, genres = fields[7], fields[8]
    if genres != SKIP_VAL and runtime != SKIP_VAL:
        # runtime = int(runtime) # no point in converting to integer
        for g in genres.strip().split(LIST_DELIMITER):
            yield g, runtime


for line in sys.stdin:
    for key, value in map_function(line):
        print(OUTPUT_FORMAT % (key, value))
