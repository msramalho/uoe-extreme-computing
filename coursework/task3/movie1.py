#!/usr/bin/python2.7

class Movie:
    def __init__(self, id=None, title=None, genres=None, decade=None, rating=None):
        self.id = id
        self.title = title
        self.genres = genres
        self.decade = decade
        self.rating = rating

    def update(self, fields):
        self.id = fields[0]
        if len(fields) == 2:            # id|rating
            self.rating = fields[1]
        else:                           # id|decade|genres|title
            self.decade = fields[1]
            self.genres = fields[2]
            self.title = fields[3]

    def _print(self): 
        if self.rating and self.decade:
            for genre in self.genres.split(","):
                # the repeated format could be removed to outside the loop
                # but that led to problems with movies that had "%" in their name
                print("%s|%s|%s|%s" % (self.decade, genre, self.title, self.rating))
        else:
            self._print_combiner()
    
    def _print_combiner(self):
        pass
    
    def parse_line(self, line):
        fields = line.strip().strip("|").split("|")
        if len(fields) == 4 and fields[0].isdigit():
            print("|".join(fields))
        elif fields[0] == self.id:  # same key
            self.update(fields)
        else:
            self._print()
            self.__init__()
            self.update(fields)