
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if nums[0] > target or nums[len(nums)-1] < target:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left//2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 5
    ret = s.search(nums, target)
    print(ret)