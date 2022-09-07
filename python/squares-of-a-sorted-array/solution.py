class Solution:
    def sortedSquares(self, nums: list) -> list:
        return sorted(list(map(self.square, nums)))

    def square(self, num):
        return (num * num)


if __name__ == '__main__':
    s = Solution()
    nums = [-4, -1, 0, 3, 10]
    r = s.sortedSquares(nums)
    print(r)
