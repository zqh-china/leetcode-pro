import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = re.compile(p)
        res = pattern.findall(s)
        if res:
            return True
        else:
            return False        



if __name__ == '__main__':
    solution = Solution()
    s = "aa"
    p = "a*"
    r = solution.isMatch(s, p)
    print(r)
