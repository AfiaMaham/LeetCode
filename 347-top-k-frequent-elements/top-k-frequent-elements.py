import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        val = list(count.values())
        heapq.heapify(val)
        maxi = heapq.nlargest(k, val)
        arr = []
        for i in count:
            if count[i] in maxi:
                arr.append(i)
        return arr