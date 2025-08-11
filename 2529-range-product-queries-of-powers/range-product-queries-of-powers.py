from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        binary = bin(n)
        power = []
        exponents = []
        binary = binary[2:]
        i = -1
        for s in binary[::-1]:
            i += 1
            if s == '1':
                power.append(2 ** i)
                exponents.append(i)  
        
       
        prefix = []
        running_sum = 0
        for e in exponents:
            running_sum += e
            prefix.append(running_sum)
        
        def mod_exp(base, exponent, mod):
            result = 1
            cur = base
            while exponent > 0:
                if exponent & 1:
                    result = (result * cur) % mod
                cur = (cur * cur) % mod
                exponent >>= 1
            return result
        
        answers = []
        for l, r in queries:
            if l == 0:
                exp_sum = prefix[r]
            else:
                exp_sum = prefix[r] - prefix[l - 1]
            
            ans = mod_exp(2, exp_sum, MOD)
            answers.append(ans)
        
        return answers


        

        