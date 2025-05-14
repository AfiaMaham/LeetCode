class Solution:
    def bitwiseComplement(self, n: int) -> int:
        new_str = ""
        bit = bin(n)
        bit = bit[2:]
        for i in bit:
            if i == "0":
                new_str += "1"
            else:
                new_str += "0"
        return int(new_str, 2)