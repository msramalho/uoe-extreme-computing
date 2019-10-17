#!/usr/bin/python2.7


class Movie:
    def __init__(self, id=None, votes=None, writer=None, known_for=None, name=None):
        self.id = id
        self.votes = votes
        self.writer = writer
        self.known_for = known_for
        self.name = name
        self.new_writer = False

    def update(self, fields):
        if len(fields) == 3:            # crew file
            self.new_writer = (self.name == None)
            self.writer = fields[2]
        else:                           # names file, len=4
            self.new_writer = (self.writer == None)
            self.known_for = fields[2]
            self.name = fields[3]

    def _print(self, change_movie=False):
        # changed_movie is True when a new "movieId|A|votes" appear
        # this is used for the combiner to know when to re-emit
        if self.name and self.writer == self.known_for:
            print("%s|%s" % (self.votes, self.name))
            self.name, self.writer = None, None # reset values 
            self._print_combiner(True, change_movie)
        else:
            self._print_combiner(False, change_movie)

    def _print_combiner(self, printed_info, change_movie):
        pass

    def parse_line(self, line):
        fields = line.strip().strip("|").split("|")
        if len(fields) == 2:
            print("%s|%s" % (fields[0], fields[1])) # re-emit from combiner
        elif fields[0] == self.id:   # same movie
            self.update(fields)
            self._print()
        elif fields[1] == "A":  # skip if A is not seen before changing key
            self._print(True)       # print the previous TODO: is this necessary?
            self.__init__(id=fields[0], votes=fields[2])
