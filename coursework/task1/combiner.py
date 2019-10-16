#!/usr/bin/python2.7

import sys
sys.path.append('./')
from statistics import Statistics

class StatisticsCombiner(Statistics):
    def _print(self):
        if self.genre != None:  
            print("%s|%d|%d|%d|%s" % (self.genre, self.sum, self.count, self.max, self.min))

stats = StatisticsCombiner()                        # create the O(1) space management object
for line in sys.stdin:
    genre, duration = line.strip().split("|", 1)
    duration = int(duration)                        # no need to test for invalid, as the value comes from mapper/combiner

    if stats.genre == genre:                        # same key
        stats.update(False, duration)
    else:                                           # new key
        stats._print()                              # print the previous
        stats = StatisticsCombiner(genre)
        stats.update(False, duration)
else:                                               # finally, print the last key
    stats._print()
