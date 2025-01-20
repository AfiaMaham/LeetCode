class Solution:
    def capitalizeTitle(self, title: str) -> str:
        arr = title.split()
        ansArray = []
        for i in arr:
            i = i.lower()
            if len(i) > 2:
                i = i.capitalize()
            ansArray.append(i)
        ans = ' '.join(ansArray)
        return ans
           
        