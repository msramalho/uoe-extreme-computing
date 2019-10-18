#!/usr/bin/python2.7

"""
Output:
genre|totalDuration|count|max|min
"""
import sys
sys.path.append('./')
from statistics import Statistics


class StatisticsCombiner(Statistics):
    def _print(self):
        if self.genre != None:
            print("%s|%d|%d|%d|%s" % (self.genre, self.sum, self.count, self.max, self.min))


stats = StatisticsCombiner()  # create the O(1) space management object
for line in sys.stdin:
    stats.parse_line(line)
else:
    stats._print()
