class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        word_set = set(wordlist)
        cap_map = {}
        vowel_map = {}

        def devowel(word):
            return ''.join('*' if c in 'aeiou' else c for c in word)

        for word in wordlist:
            lower = word.lower()
            if lower not in cap_map:
                cap_map[lower] = word
            dv = devowel(lower)
            if dv not in vowel_map:
                vowel_map[dv] = word

        res = []
        for q in queries:
            if q in word_set:
                res.append(q)
                continue
            lower = q.lower()
            if lower in cap_map:
                res.append(cap_map[lower])
                continue
            dv = devowel(lower)
            if dv in vowel_map:
                res.append(vowel_map[dv])
                continue
            res.append("")
        return res
