#!/usr/bin/python2.7

import sys
import heapq as H

# Note that this heap will have a constant memory space of max 10 (internally could be 11 during heappushpop)
heap = [(-1, "")]*10
H.heapify(heap)

last_a = {}

for line in sys.stdin:
    fields = line.strip().strip("|").split("|")
    if len(fields)==2: # combiner
        H.heappushpop(heap, (int(fields[0]), fields[1]))
    elif fields[1] == "A":
        # movie_id, {writers}, votes
        last_a = {"id": fields[0], "writers": set(fields[2].split(",")), "votes": int(fields[3])}
    elif len(last_a): # if "B"
        # if non-matching Ids or known_for not writer
        if fields[0] != last_a["id"] or fields[2] not in last_a["writers"]: continue
        t = (last_a["votes"], fields[3])
        H.heappushpop(heap, t)
    # print(heap)
#TODO: non-duplicate name
for writer in sorted(heap, reverse=True):
    print("%s|%s" % writer)
