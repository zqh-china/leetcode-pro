class Solution:
    def romanToInt(self, s):
        ref = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s_sum = 0
        pre_num = ref[s[0]]
        for i in range(1, len(s)):
            num = ref[s[i]]
            if pre_num < num:
                s_sum -= pre_num
            else:
                s_sum += pre_num
            pre_num = num
        s_sum += pre_num
        return s_sum




# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


if __name__ == '__main__':
    s = Solution()
    r = s.romanToInt('LVIII')
    print(r)