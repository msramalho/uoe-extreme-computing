#!/usr/bin/python2.7


class Movie:
    def __init__(self, id=None, votes=None, writer=None, known_for=None, name=None):
        self.id = id
        self.votes = votes
        self.writer = writer
        self.known_for = known_for
        self.name = name

    def update(self, fields):
        if len(fields) == 3:            # crew file
            if self.writer: self._print_combiner_b()
            self.writer = fields[2]
        else:                           # names file, len=4
            if self.known_for: self._print_combiner_b()
            self.known_for = fields[2]
            self.name = fields[3]

    def _print(self):
        if self.name and self.writer == self.known_for:
            print("%s|%s" % (self.votes, self.name))
            self.__init__(self.id, self.votes)

    def _print_combiner_a(self): pass
    def _print_combiner_b(self): pass
    def _print_combiner_default(self, line): pass

    def parse_line(self, line):
        fields = line.strip().strip("|").split("|")
        if len(fields) == 2:
            # print("%s|%s" % (fields[0], fields[1]))  # re-emit from combiner
            pass
        elif fields[1] == "A":                      # skip if A is not seen before changing key
            self._print_combiner_a()
            self._print()
            self.__init__(id=fields[0], votes=fields[2])
        elif fields[0] == self.id:                  # same movie
            self.update(fields)
            self._print()
        else:
            self._print_combiner_default(line)
