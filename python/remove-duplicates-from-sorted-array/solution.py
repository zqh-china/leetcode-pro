

# 这种方法是没有考虑数组是有序的
# class Solution:
#     def removeDuplicates(self, nums: list) -> int:
#         i = 0
#         while i < len(nums) - 1:
#             j = i
#             while j < len(nums) - 1:
#                 if nums[j] == nums[j+1]:
#                     nums.pop(j)
#                     j -= 1
#                 j += 1
#             i += 1
#         return len(nums)

class Solution:
    def removeDuplicates(self, nums: list) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
                i -= 1
            i += 1
        return len(nums)






if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2]
    r = s.removeDuplicates(nums)
    print(r)
    print(nums)