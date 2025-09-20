from collections import deque, defaultdict
import bisect

class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.queue = deque()
        self.seen = set()
        self.dest_map = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.seen:
            return False
        if len(self.queue) == self.limit:
            old_source, old_dest, old_time = self.queue.popleft()
            self.seen.remove((old_source, old_dest, old_time))
            arr = self.dest_map[old_dest]
            idx = bisect.bisect_left(arr, old_time)
            if idx < len(arr) and arr[idx] == old_time:
                arr.pop(idx)
            if not arr:
                del self.dest_map[old_dest]
        self.queue.append((source, destination, timestamp))
        self.seen.add(key)
        bisect.insort(self.dest_map[destination], timestamp)
        return True

    def forwardPacket(self) -> list[int]:
        if not self.queue:
            return []
        source, dest, time = self.queue.popleft()
        self.seen.remove((source, dest, time))
        arr = self.dest_map[dest]
        idx = bisect.bisect_left(arr, time)
        if idx < len(arr) and arr[idx] == time:
            arr.pop(idx)
        if not arr:
            del self.dest_map[dest]
        return [source, dest, time]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_map:
            return 0
        arr = self.dest_map[destination]
        l = bisect.bisect_left(arr, startTime)
        r = bisect.bisect_right(arr, endTime)
        return r - l
