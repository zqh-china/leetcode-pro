

v = 4

def isBadVersion(version: int) -> bool:
    return version == v

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    solution = Solution()
    r = solution.firstBadVersion(5)
    print(r)
            
