class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        new_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        string = ''
        for k, v in new_dict.items():
            for i in range(v):
                string += k
        return string
        