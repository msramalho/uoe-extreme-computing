#!/usr/bin/python2.7

import sys

# global variables
# [avg runtime:float|max runtime:int|min runtime:int|genre:str]
OUTPUT_FORMAT = "%.2f|%d|%d|%s"
MAX_DURATION = 2**32  # naturally, a smaller number could be used


# class for logic isolation and readability
class Statistics:
    def __init__(self, genre=None, _min=MAX_DURATION, _max=0, _sum=0, count=0):
        self.genre = genre
        self.min = _min
        self.max = _max
        self.sum = _sum
        self.count = count

    def update(self, duration):
        # perform the statistics update for this genre based on the new duration value
        self.min = min(self.min, duration)
        self.max = max(self.max, duration)
        self.sum += duration
        self.count += 1

    def average(self):
        # calculate the average for the duration
        return float(self.sum) / self.count if self.count > 0 else 0

    def _print(self):
        # print the statistics if this is a valid genre
        if self.genre != None:
            print(OUTPUT_FORMAT % (self.average(), self.max, self.min, self.genre))


stats = Statistics()                                # create the O(1) space management object
for line in sys.stdin:
    genre, duration = line.strip().split("|", 1)
    duration = int(duration)                        # no need to test for invalid, as the value comes from mapper/combiner

    if stats.genre == genre:                        # same key
        stats.update(duration)
    else:                                           # new key
        stats._print()                              # print the previous
        stats = Statistics(genre)
        stats.update(duration)
else:                                               # finally, print the last key
    stats._print()
