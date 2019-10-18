#!/usr/bin/python2.7

import sys
sys.path.append('./')
from statistics import Statistics
# NOTE: combiner and mapper could have the same output format (and simpler implementation), 
# but that would imply more data sent from raw map output over the network
# as such mappers output "genre|duration" and combiners "genre|totalDuration|count|max|min"
# in an effort to reduce network traffic and use combiners at the same time


stats = Statistics() # create the O(1) space management object
for line in sys.stdin:
    stats.parse_line(line)
else:
    stats._print()
