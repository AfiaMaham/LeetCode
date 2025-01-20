class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        w = ""
        for i in words:
            w += i[0]
        if w == s:
            return True
        else:
            return False

        