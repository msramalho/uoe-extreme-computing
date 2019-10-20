#!/usr/bin/python2.7


class Movie:
    def __init__(self, id=None, votes=None, writers=None):
        self.id = id
        self.votes = votes
        self.writers = writers

    def update(self, fields):
        # self.id = fields[0]
        if unicode(fields[1]).isnumeric():      # ratings file
            self.votes = fields[1]
        else:                                   # crew file
            self.writers = fields[1]

    def _print(self):
        if self.votes and self.writers:
            print("%s|%s|%s" % (self.id, self.writers, self.votes))
            self.__init__(self.id)

    def parse_line(self, line):
        fields = line.strip().strip("|").split("|")
        if len(fields) == 3:  # from combiner
            print(line.strip())
        else:
            if self.id == fields[0]:
                self.update(fields)
                self._print()
            else:
                self.__init__(fields[0])
                self.update(fields)
