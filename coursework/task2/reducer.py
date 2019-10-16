#!/usr/bin/python2.7

"""
Output: 
    [Title]
"""
import sys
sys.path.append('./')
from movie import Movie

class MovieReducer(Movie):
    def _print(self):
        # print title if valid and all filters have been checked
        if self.id and self.filter1 and self.filter2:
            print(self.title)


movie = MovieReducer()
for line in sys.stdin:
    parts = line.strip().strip("|").split("|", 1)
    if len(parts) == 1: # combiner output
        print(parts[0])
    else:               # mapper output
        id, value = parts
        if movie.id == id:  # same key
            movie.update_filter(value)
        else:
            movie._print()
            movie = MovieReducer(id)
            movie.update_filter(value)
else:  # finally, print the last movie
    movie._print()

