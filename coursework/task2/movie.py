#!/usr/bin/python2.7


class Movie:
    def __init__(self, id=None, filter1=False, filter2=False, title=None):
        self.id = id
        self.filter1 = filter1
        self.filter2 = filter2
        self.title = title

    def update_filter(self, value):
        # update the filter according to the received key
        if value == "B":             # ratings.tsv mapper
            self.filter2 = True
        else:                       # basics.tsv mapper
            self.filter1 = True
            self.title = value[1:]  # Recover the movieTitle by removing the 'A'
    
    def update_from_line(self, line):
        pass

