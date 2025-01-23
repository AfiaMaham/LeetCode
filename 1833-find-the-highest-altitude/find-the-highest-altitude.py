class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0] 
        for i in range(len(gain)):
            x = altitudes[i] + gain[i]
            altitudes.append(x)
        return max(altitudes)