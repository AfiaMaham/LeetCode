class Solution:
    def addDigits(self, num: int) -> int:
        str1 = str(num)
        while len(str1) > 1:
            str1 = str(num)
            list1 = list(str1)
            a = 0
            for i in list1:
                a += int(i)
            num = a
                
        return num


        