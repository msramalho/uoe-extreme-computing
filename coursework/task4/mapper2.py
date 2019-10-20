#!/usr/bin/python2.7

"""
Input:                         From:
writerId|movieId|votes         reducer1
{Person}                       name.basics.tsv
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


# name.basics.tsv related code
def map_names(fields):
    Person = namedtuple('Person', 'id name birth death profession known_for')
    p = Person(*fields)
    if validate(p, ["name", "known_for"]):
        for movie in p.known_for.split(","):
            yield "%s|B|%s|%s" % (movie, p.id, p.name)

def map_prev(fields):
    yield "%s|A|%s|%s" % tuple(fields)

def map_function(line):
    line = line.strip()
    fields = line.split(DATA_DELIMITER)
    if len(fields) == 6: return map_names(fields)
    else: 
        fields = line.split("|")
        return map_prev(fields)

for line in sys.stdin:
    for m in map_function(line):
        _print(m)