import heapq as H


class Writer:
    def __init__(self):
        self.last_a = {}  # {movie_id:_, writers:[], votes:_}
        # Note that this self.heap will have a constant memory space of max 10 (internally could be 11 during heappushpop)
        self.heap = [(-1, "")] * 10
        H.heapify(self.heap)

    def _print_combiner_a(self): pass
    def _print_combiner_b(self, fields): pass

    def not_duplicate(self, tup):
        # avoid duplicate writer names
        tmp = self.heap[::]
        self.heap = []
        dup = False
        for votes, writer in tmp:
            if writer == tup[1]:
                dup = True
                self.heap.append((max(votes, tup[0]), writer))
            else:
                self.heap.append((votes, writer))
        H.heapify(self.heap)
        # if the writer name was new update heap
        if not dup:
            H.heappushpop(self.heap, tup)

    def parse_line(self, line):
        fields = line.strip().strip("|").split("|")
        # if len(fields) == 1: return
        if len(fields) == 2:  # combiner
            self.not_duplicate((int(fields[0]), fields[1]))
        elif fields[1] == "A":
            self._print_combiner_a()
            self.last_a = {"id": fields[0], "writers": set(fields[2].split(",")), "votes": int(fields[3])}

        else:  # if "B"
            # if non-matching Ids or known_for not writer
            if not len(self.last_a) or fields[0] != self.last_a["id"]:
                self._print_combiner_b(fields)
                return
            elif fields[2] not in self.last_a["writers"]: return
            t = (self.last_a["votes"], fields[3])
            self.not_duplicate(t)

    def _print_result(self):
        # TODO: non-duplicate name
        for writer in sorted(self.heap, reverse=True):
            if writer[0] >= 0:  # ignore "-1|"
                print("%s|%s" % writer)
