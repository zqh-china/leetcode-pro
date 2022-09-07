class Solution:
    def longestCommonPrefix(self, strs):
        # min_len = 200
        # min_index = 0
        # for i in range(len(strs)):
        #     if min_len > len(strs[i]):
        #         min_len = len(strs[i])
        #         min_index = i
        # cmstr = strs[min_index]
        cmstr = strs[0]
        longest_common_prefix = ""
        for i in range(len(cmstr)):
            common_prefix = cmstr[i]
            for j in range(1, len(strs)):
                if len(strs[j]) == i:
                    return longest_common_prefix
                if common_prefix != strs[j][i]:
                    return longest_common_prefix
            longest_common_prefix += common_prefix
        return longest_common_prefix
        


if __name__ == '__main__':
    s = Solution()
    # strs = ["flower","flow","flight"]
    strs = ["ab", "a"]
    r = s.longestCommonPrefix(strs)
    print(r)
