class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        ref = {'(': ')', '[': ']', '{': '}', ')': '', ']': '', '}': ''}
        for i in range(len(s)):
            curr = s[i]
            if stack:
                peak = stack[-1]
                
                if ref[peak] == curr:
                    stack.pop()
                else:
                    stack.append(curr)
            else:
                stack.append(curr)
        if stack:
            return False
        else:
            return True







if __name__ == '__main__':
    s = Solution()
    r = s.isValid('())))(((')
    print(r)