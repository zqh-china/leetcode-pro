from pickletools import read_uint1


class Solution:
    def mySqrt(self, x: int) -> int:
        num = 1
        while num * num < x:
            num += 1
        if num * num == x:
            return num
        return num - 1

# 二分查找
class Solution2:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        min = 0
        max = x
        while max > min + 1:
            m = (max + min) // 2
            if x//m >= m:
                min = m
            else:
                max = m
        return min

# 牛顿迭代法
class Solution3:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        x0 = x
        c = x
        while True:
            xi = 0.5 *(x0 + c/x0)
            if abs(xi-x0) < 1e-6:
                break
            x0 = xi
        return int(x0)


if __name__ == '__main__':
    s = Solution3()
    r = s.mySqrt(15)
    print(r)