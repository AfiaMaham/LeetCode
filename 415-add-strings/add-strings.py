import sys
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(50000)
        sum = str(int(num1) + int(num2))
        return sum
