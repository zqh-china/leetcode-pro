
class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1
        for i in range(len(s)//2):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    solution = Solution()
    solution.reverseString(s)
    print(s)