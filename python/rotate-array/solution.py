class Solution:
    def rotate(self, nums: list, k: int) -> None:
        k = k % len(nums)
        if k != 0 and len(nums) != 1:
            right = nums[-k:]
            left = nums[:-k]
            nums[:k] = right
            nums[k:] = left


if __name__ == '__main__':
    nums = [1, 2]
    k = 2
    s = Solution()
    s.rotate(nums, k)
    print(nums)
