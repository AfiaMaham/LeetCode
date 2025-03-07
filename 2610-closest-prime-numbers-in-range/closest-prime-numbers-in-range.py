import sys
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve_of_eratosthenes(n):
            primes = [True] * (n + 1)  
            primes[0] = primes[1] = False  

            for p in range(2, int(n**0.5) + 1):
                if primes[p]: 
                    for multiple in range(p * p, n + 1, p): 
                        primes[multiple] = False
            return [num for num in range(left, right+1) if primes[num]]  

        ans = sieve_of_eratosthenes(right)
        if len(ans) <= 1:
            return [-1, -1]
        count = 10**10
        pair = []
        for i in range(len(ans)-1 ):
            x = ans[i+1] - ans[i]
            if x < count:
                count = x
                pair = [ans[i], ans[i+1]]
        return pair