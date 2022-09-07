# class Solution:
#     def runningSum(self, nums: list) -> list:
#         ret = []
#         for i in range(1, len(nums)+1):
#             ret.append(sum(nums[:i]))
#         return ret

class Solution:
    def runningSum(self, nums: list) -> list:
        ret = [0] * len(nums)
        ret[0] = nums[0]
        for i in range(1, len(nums)):
            ret[i] = ret[i-1] + nums[i]
        return ret



if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    r = s.runningSum(nums)
    print(r)