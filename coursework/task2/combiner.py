#!/usr/bin/python2.7

import sys
sys.path.append('./')
from movie import Movie


class MovieCombiner(Movie):
    def _print(self):
        # print title if valid and all filters have been checked
        if self.id:
            if self.filter1 and self.filter2:
                print(self.title)
            elif self.title:  # aka filter1
                print("%s|A%s" % (self.id, self.title))
            else:
                print("%s|B" % self.id)


movie = MovieCombiner()
for line in sys.stdin:
    parts = line.strip().strip("|").split("|", 1)
    if len(parts) == 1:  # combiner output
        print(parts[0])
    else:               # mapper output
        id, value = parts
        if movie.id == id:  # same key
            movie.update_filter(value)
        else:
            movie._print()
            movie = MovieCombiner(id)
            movie.update_filter(value)
else:  # finally, print the last movie
    movie._print()
