
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lh = len(haystack)
        ln = len(needle)
        if lh < ln:
            return -1
        if lh == ln:
            if haystack == needle:
                return 0
            else:
                return -1
        
        for i in range(lh-ln+1):
            pice = haystack[i:i+ln]
            if pice == needle:
                return i
        return -1





if __name__ == '__main__':
    s = Solution()
    r = s.strStr('abc', 'c')
    print(r)