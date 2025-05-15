class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        new_str = ""
        shift = 0
        shifts.reverse()
        s = s[::-1]
        for i in range(len(shifts)):
            shift += shifts[i]
            ascii_num = ord(s[i]) + shift
            if ascii_num > 122:
                val = ascii_num - 122
                q = val//26
                val -= (26*q)
                if val == 0:
                    ascii_num = 122
                else:
                    ascii_num = 96 + val
            ch = chr(ascii_num)
            new_str += ch

        return new_str[::-1]



            
                
            
