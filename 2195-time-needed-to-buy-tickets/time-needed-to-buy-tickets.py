from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque(tickets)
        sec = 0
        while q[k] != 0:
            num = q.popleft()
            num = num - 1
            if k == 0 and num == 0:
                return sec+1
            if num != 0:
                q.append(num)
            sec += 1
            if k == 0:
                k = len(q)-1
            else:
                k = k-1

        return sec