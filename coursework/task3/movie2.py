#!/usr/bin/python2.7

class Movie:
    def __init__(self, decade=None, genre=None, title=None, rating=-1):
        self.decade = decade
        self.genre = genre
        self.title = title
        self.rating = rating

    def update(self, fields):
        self.decade = fields[0]
        self.genre = fields[1]
        new_rating = float(fields[3])
        if self.rating < new_rating:    # if the new film has higher rating
            self.rating = new_rating    # update the max rating
            self.title = fields[2]      # and the corresponding title

        # NOTE: there is no need to check for rating == new_rating
        # since this reducer receives the movie names in lexicographical order
        # and so this will always yield the first movie alphabetically

    def is_same(self, fields):
        return self.decade == fields[0] and self.genre == fields[1]

    def _print(self):
        # print result if movie info is present
        if self.title:
            print("%s|%s|%s" % (self.decade, self.genre, self.title))

    def parse_line(self, line):
        fields = line.strip().strip("|").split("|")
        if self.is_same(fields):  # same decade and genre
            self.update(fields)
        else:
            self._print()
            self.__init__()
            self.update(fields)
