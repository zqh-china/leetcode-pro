class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        i = 0
        while True:
            if i == len(nums):
                break
            if nums[i] == val:
                nums.pop(i)
                i -= 1
            i += 1

        
        return i


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4, 3, 3, 2]
    r = s.removeElement(nums, 3)
    print(r)
    print(nums)