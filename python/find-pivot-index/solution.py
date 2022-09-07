class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left = 0
        print(left)
        right = sum(nums[1:])
        for i in range(len(nums)-1):
            if left == right:
                return i
            left += nums[i]
            right -= nums[i+1]
        if left == right:
            return len(nums) - 1
        return -1

if __name__ == '__main__':
    s = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    r = s.pivotIndex(nums)
    print(r)