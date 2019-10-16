#!/usr/bin/python2.7

import sys
sys.path.append('./')
from statistics import Statistics
# NOTE: combiner and mapper could have the same format, 
# but that would imply more data sent from raw map output over the network
# as such mappers output genre|duration and combiners genre|totalDuration|count|max|min
# in an effort to reduce network traffic and use combiners at the same time


class StatisticsReducer(Statistics):
    def _print(self):
# [avg runtime:float|max runtime:int|min runtime:int|genre:str]
        if self.genre != None:
            print("%.2f|%d|%d|%s" % (self.average(), self.max, self.min, self.genre))

stats = StatisticsReducer()                         # create the O(1) space management object
for line in sys.stdin:
    # print(line)
    
    parts = line.strip().strip("|").split("|")
    genre = parts[0]
    from_combiner = len(parts) > 2                  # 2 is from mapper
    args = [from_combiner] + [int(p) for p in parts[1:]]
    
    # update regardless of map or combiner output :)
    if stats.genre == genre:                        # same key
        stats.update(*args)
    else:                                           # new key
        stats._print()                              # print the previous
        stats = StatisticsReducer(genre)
        stats.update(*args)
else:                                               # finally, print the last key
    stats._print()
