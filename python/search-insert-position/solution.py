class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            if target < nums[i]:
                    return i
            if i+1 < len(nums):
                if target > nums[i] and target < nums[i+1]:
                    return i + 1
                
        return i+1

if __name__ == '__main__':
    s = Solution()
    nums = [2,3,5,6]
    target = 3
    r = s.searchInsert(nums, target)
    print(r)