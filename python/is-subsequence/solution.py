false = False
true = True

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        if len(s) > len(t) or (len(s) == len(t) and s != t): 
            return False
        s_curr = 0
        t_curr = 0
        for i in range(len(t)):
            if s[s_curr] == t[t_curr]:
                s_curr += 1
            t_curr += 1
            if s_curr == len(s):
                return true
        return false

if __name__ == "__main__":
    solution = Solution()
    s = "abc"
    t = "ahbgdc"
    r = solution.isSubsequence(s, t)
    print(r)

