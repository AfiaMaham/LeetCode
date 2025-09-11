class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        v = sorted([c for c in s if c in vowels])
        it = iter(v)
        res = []
        for c in s:
            if c in vowels:
                res.append(next(it))
            else:
                res.append(c)
        return "".join(res)
