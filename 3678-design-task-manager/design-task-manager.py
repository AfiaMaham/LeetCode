import heapq
from typing import List

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_map = {}
        self.heap = []
        for u, t, p in tasks:
            self.task_map[t] = (u, p)
            heapq.heappush(self.heap, (-p, -t, u))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        u, _ = self.task_map[taskId]
        self.task_map[taskId] = (u, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, u))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self) -> int:
        while self.heap:
            p, t, _ = heapq.heappop(self.heap)
            taskId = -t
            if taskId in self.task_map and self.task_map[taskId][1] == -p:
                userId = self.task_map[taskId][0]
                del self.task_map[taskId]
                return userId
        return -1
