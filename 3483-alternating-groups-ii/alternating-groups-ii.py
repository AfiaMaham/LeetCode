from collections import defaultdict

class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        n = len(colors)
        colors.extend(colors[:k - 1])
        mp = defaultdict(int)
        vi = -1  # Violating index
        i, j = 0, 0
        count = 0
        
        while j < len(colors):
            if j > 0 and colors[j - 1] == colors[j]:
                vi = j
            mp[colors[j]] += 1
            
            if j - i + 1 < k:
                j += 1
            else:
                mp[colors[i]] -= 1
                i += 1
                j += 1
                if vi >= i and vi <= j:
                    continue
                count += 1
        
        return count
