# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         i = 1
#         flag = False
#         while i ** 2 <= num:
#             if i ** 2 == num:
#                 flag = True
#             i += 1
#         return flag

# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         return num ** 0.5 % 1 == 0


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square < num:
                left = mid + 1
            elif square > num:
                right = mid - 1
            else:
                return True
        return False



if __name__ == '__main__':
    s = Solution()
    num = 43245
    ret = s.isPerfectSquare(num)
    print(ret)

