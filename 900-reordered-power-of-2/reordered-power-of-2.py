class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        target = ''.join(sorted(str(n)))
        
        for i in range(30):  
            if ''.join(sorted(str(1 << i))) == target:
                return True
        return False
