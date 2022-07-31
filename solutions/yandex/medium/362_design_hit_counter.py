# Design a hit counter which counts the number of hits received in the past 5 minutes. Each function accepts
# a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system
# in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest
# timestamp starts at 1. It is possible that several hits arrive roughly at the same time.
# Follow up: What if the number of hits per second could be very large? Does your design scale?


class HitCounter:
    def __init__(self):
        self.timestamps, self.hits = [0] * 300, [0] * 300

    def hit(self, timestamp: int) -> None:
        i = timestamp % 300
        if self.timestamps[i] == timestamp:
            self.hits[i] += 1
        else:
            self.timestamps[i], self.hits[i] = timestamp, 1

    def getHits(self, timestamp: int) -> int:
        return sum(h for t, h in zip(self.timestamps, self.hits) if timestamp - t < 300)
