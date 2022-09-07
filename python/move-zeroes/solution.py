# class Solution:
#     def moveZeroes(self, nums: list) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # for i in range(len(nums)):
#         #     for j in range(i, len(nums)-1):
#         #         if nums[j] == 0 and nums[j+1] != 0:
#         #             nums[j+1], nums[j] = nums[j], nums[j+1]
#         length = len(nums)
#         z_count = nums.count(0)
#         nz_count = length - z_count
#         nz_nums = [num for num in nums if num != 0]
#         nums[:nz_count] = nz_nums
#         nums[nz_count:] = [0] * z_count

class Solution:
    def moveZeroes(self, nums: list) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1



if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 1, 0, 0, 0]
    s.moveZeroes(nums)
    print(nums)
