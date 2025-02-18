class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        i = 1
        while i <= n:
            if n % i == 0:
                count += 1
            i += 1
        if count == 3:
            return True
        else:
            return False