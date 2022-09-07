# 0557
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words_reversed = list(map(self.reverseWord, words))
        return " ".join(words_reversed)

    def reverseWord(self, w: str) -> str:
        return w[::-1]

if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    solution = Solution()
    ret = solution.reverseWords(s)
    print(len(ret))
    print(len(ret.strip()))
