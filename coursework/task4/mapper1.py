#!/usr/bin/python2.7

"""
Output:                                 Input:
    movieId|A|votes                     title.ratings.tsv
    movieId|B|personId|personName       name.basics.tsv
    movieId|B|writerId                  title.crew.tsv
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
    # no filtering required, just output id|A|votes -> A will be used for secondary sorting
    yield "%s|A|%s" % (fields[0], fields[2])


# name.basics.tsv related code
def map_names(fields):
    Person = namedtuple('Person', 'id name birth death profession known_for')
    p = Person(*fields)
    if validate(p, ["name", "known_for"]):
        for movie in p.known_for.split(","):
            yield "%s|B|%s|%s" % (movie, p.id, p.name) # B for sorting after A


# crew.tsv related code
def map_crew(fields):
    Crew = namedtuple('Crew', 'movie_id directors writers')
    c = Crew(*fields)
    if validate(c, ["writers"]):
        for writer in c.writers.split(","):
            yield "%s|B|%s" % (c.movie_id, writer) # B for sorting after A


# main code
def map_function(line):
    # split line and return according to input type (basics, ratings)
    fields = line.strip().split(DATA_DELIMITER)
    if len(fields) == 6: return map_names(fields)
    elif str.isdigit(fields[2]): return map_ratings(fields)
    else: return map_crew(fields)


for line in sys.stdin:
    for out in map_function(line):
        _print(out)