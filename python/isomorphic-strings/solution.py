

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        hashmap2 = {}
        for i in range(len(s)):
            if (hashmap.get(s[i]) is not None and hashmap.get(s[i]) != t[i]) or hashmap2.get(t[i]) is not None and hashmap2.get(t[i]) != s[i]:
                return False
            
            hashmap[s[i]] = t[i]
            hashmap2[t[i]] = s[i]
        return True     


if __name__ == '__main__':
    solution = Solution()
    s = 'badc'
    t = 'baba'
    r = solution.isIsomorphic(s, t)
    print(r)
        