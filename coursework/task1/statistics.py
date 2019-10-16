
# global variables
# [avg runtime:float|max runtime:int|min runtime:int|genre:str]
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
        if from_combiner:
            self.min = min(self.min, _min)
            self.max = max(self.max, _max)
            self.count += count
        else:
            self.min = min(self.min, duration)
            self.max = max(self.max, duration)
            self.count += 1

    def average(self):
        # calculate the average for the duration
        return float(self.sum) / self.count if self.count > 0 else 0