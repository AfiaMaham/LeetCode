class Solution:
    def makeGood(self, s: str) -> str:
        good = []
        for i in s:
            if good and ((i.isupper() and good[-1] == i.lower()) or (i.islower() and good[-1] == i.upper())):
                good.pop()
            else:
                good.append(i)
        return "".join(good)