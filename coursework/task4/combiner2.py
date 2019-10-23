#!/usr/bin/python2.7

import sys
sys.path.append('./')
from writer import Writer

class WriterCombiner(Writer):
    def _print_combiner_a(self): 
        a = self.last_a
        if not len(a): return
        print("%s|A|%s|%s" % (a["id"], ",".join(a["writers"]), a["votes"]))

    def _print_combiner_b(self, fields):
        print("%s|B|%s|%s" % (fields[0], fields[2], fields[3]))


w = WriterCombiner()
for line in sys.stdin:
    w.parse_line(line)
else:
    w._print_combiner_a()
w._print_result()
