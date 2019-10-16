#!/usr/bin/python2.7


class Movie:
    def __init__(self, id=None, filter1=False, filter2=False, title=None):
        self.id = id
        self.filter1 = filter1
        self.filter2 = filter2
        self.title = title

    def update_filter(self, value):
        # update the filter according to the received key
        if value == "B":            # ratings.tsv mapper
            self.filter2 = True
        else:                       # basics.tsv mapper
            self.filter1 = True
            self.title = value[1:]  # Recover the movieTitle by removing the 'A'

    def _print(self):
        # print title if valid and all filters have been checked
        if self.id and self.filter1 and self.filter2:
            print(self.title)
        else:
            self._print_combiner()

    def _print_combiner(self):
        pass

    def parse_line(self, line):
        parts = line.strip().strip("|").split("|", 1)
        if len(parts) == 1:  # combiner output
            print(parts[0])
        else:               # mapper output
            id, value = parts
            if self.id == id:  # same key
                self.update_filter(value)
            else:
                self._print()
                self.__init__(id)
                self.update_filter(value)
