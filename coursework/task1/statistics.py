#!/usr/bin/python2.7

# global variables
MAX_DURATION = 2**32  # naturally, a smaller number could be used


# class for logic isolation and readability
class Statistics:
    def __init__(self, genre=None, _min=MAX_DURATION, _max=0, _sum=0, count=0):
        self.genre = genre
        self.min = _min
        self.max = _max
        self.sum = _sum
        self.count = count

    def update(self, from_combiner, duration, count=None, _max=None, _min=None):
        # perform the statistics update for this genre based on the new duration value
        self.sum += duration
        if from_combiner:                   # line from combiner output
            self.min = min(self.min, _min)
            self.max = max(self.max, _max)
            self.count += count
        else:                               # line from mapper
            self.min = min(self.min, duration)
            self.max = max(self.max, duration)
            self.count += 1

    def average(self):
        # calculate the average for the duration
        return float(self.sum) / self.count if self.count > 0 else 0

    def _print(self):
        # [avg runtime:float|max runtime:int|min runtime:int|genre:str]
        if self.genre != None:
            print("%.2f|%d|%d|%s" % (self.average(), self.max, self.min, self.genre))

    def parse_line(self, line):
        parts = line.strip().strip("|").split("|")
        genre = parts[0]
        from_combiner = len(parts) > 2  # 2 is from mapper
        args = [from_combiner] + [int(p) for p in parts[1:]]

        # update regardless of map or combiner output :)
        if self.genre == genre:     # same key
            self.update(*args)
        else:                       # new key
            self._print()           # print the previous
            self.__init__(genre)
            self.update(*args)
