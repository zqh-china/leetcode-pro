class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1
        while True:
            pass


if __name__ == '__main__':
    solution = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    ret = solution.searchRange(nums, target)
    print(ret)