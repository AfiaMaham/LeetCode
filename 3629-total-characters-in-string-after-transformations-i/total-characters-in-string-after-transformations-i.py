class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        arr = []
        MOD = 10**9 + 7
        alp = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(alp)):
            arr.append(s.count(alp[i]))
        
        for i in range(t):
            new_arr = [0] *26
            for j in range(len(arr)):
                if j == 25:
                    new_arr[0] += arr[j] % MOD
                    new_arr[1] += arr[j] % MOD
                else:
                    new_arr[j+1] += arr[j] % MOD
            arr = new_arr

        return sum(arr) % MOD


        
        # new_str = ""
        # l = 0
        # for i in range(len(s)):
        #     ascii_value = ord(s[i]) + t
        #     if ascii_value > 122:
        #         diff = 123 - ord(s[i])
        #         rem =  t - diff
        #         l += 2
        #         rem = rem // 26
        #         rem *= 2
        #         l += rem
        #     else:
        #         l += 1
        # return l

