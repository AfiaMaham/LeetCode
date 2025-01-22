class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ""
        str2 = ""
        for x in word1:
            str1 += x
        for x in word2:
            str2 += x
        if str1 == str2:
            return True
        else:
            return False