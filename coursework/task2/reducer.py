#!/usr/bin/python2.7

"""
Output: 
Title
"""
import sys
sys.path.append('./')
from movie import Movie

movie = Movie()
for line in sys.stdin:
    movie.parse_line(line)
else:
    movie._print()
