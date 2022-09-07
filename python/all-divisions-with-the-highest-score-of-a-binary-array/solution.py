class Solution:
    def maxScoreIndices(self, nums):
        score_index = [0]
        score_sum = 0
        max_score_sum = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                score_sum += 1
                if score_sum > max_score_sum:
                    max_score_sum = score_sum
                    score_index = [i + 1]
                elif score_sum == max_score_sum:
                    score_index.append(i + 1)
            else:
                score_sum -= 1

        return score_index


if __name__ == '__main__':
    nums = [1, 0, 1, 0, 1, 1, 0, 1, 0]
    solution = Solution()
    ret = solution.maxScoreIndices(nums)
    print(ret)
