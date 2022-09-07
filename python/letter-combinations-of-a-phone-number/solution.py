class Solution:
    def letterCombinations(self, digits: str) -> list:
        if not digits:
            return []
        ref = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"], 
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"]
        }
        ret = []
        for i in range(len(digits)):
            num = digits[i]
            ret.append(ref[num])
            if len(ret) == 2:
                part2 = ret.pop()
                part1 = ret.pop()
                ret.append(self.combinate(part1, part2))
        return ret[0]

    def combinate(self, part1, part2):
        ret = []
        for i in range(len(part1)):
            for j in range(len(part2)):
                ret.append(f"{part1[i]}{part2[j]}")
        return ret



if __name__ == '__main__':
    s = Solution()
    digits = "23"
    r = s.letterCombinations(digits)
    print(r)
