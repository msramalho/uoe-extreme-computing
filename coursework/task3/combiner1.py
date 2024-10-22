#!/usr/bin/python2.7

"""
Output (reduced):
decade|genre|title|rating

Output (re-emitted):
id|rating
id|decade|genre|title
"""
import sys
sys.path.append('./')
from movie1 import Movie


class MovieCombiner(Movie):
    def _print_combiner(self):
        # method called in case _print is unsuccessful, meaning the map outputs should be re-emitted
        if self.rating:  # only has id|rating
            print("%s|%s" % (self.id, self.rating))
        elif self.genres:  # has id|decade|genres|title
            print("%s|%s|%s|%s" % (self.id, self.decade, self.genres, self.title))


m = MovieCombiner()
for line in sys.stdin:
    m.parse_line(line)
else:
    m._print()
