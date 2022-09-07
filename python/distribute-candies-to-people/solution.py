# 分糖果问题
# 感觉是一个有关斐波那契数列的问题，糖果数量要么是斐波那契数列中的数，要么在斐波那契数列中的两个数之间

# 三角形数

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, ...

# an - an-1 = bn
# bn = {2, 3, 4, 5, 6, 7, ...} = 1 + n
# an -an-1 = 1 + n
# an-1 - an-2 = n
# an-2 - an-3 = n-1
# a2 - a1 = 3
# an - a1 = (3 + 1 + n)*(n - 1)/2 = 1/2 (n^2 + 3n - 4) 
# an = 1/2 (n^2 + 3n - 4) + 1




from subprocess import list2cmdline


class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        s = 0
        i = 1
        nums = []
        while True:
            nums.append(i)
            s += i
            if s > candies:
                s  -= i
                break
            i += 1
        peoples = [0] * num_people 
        rtimes = (i-1)//num_people
        # print(nums)
        for j in range(rtimes+1):
            if (j+1) * num_people >= len(nums):
                rnd = nums[j*num_people:-1] + [candies-s]
            else:
                rnd = nums[j*num_people:(j+1)*num_people]
            # print(rnd)
            df = len(peoples)-len(rnd)
            if df > 0:
                rnd += [0] * df
            tmp = zip(peoples, rnd)
            peoples = list(map(sum, tmp))
        
        return peoples



    def getNumList(self, n):
        numList = [int((i*i + 3*i -4)/2 + 3) for i in range(n)]
        return numList

if __name__ =='__main__':
    s = Solution()
    r = s.distributeCandies(900, 40)

    print(r)
