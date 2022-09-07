class Solution:
    def myAtoi(self, s):
        s = s.strip()  # 移除多余的空格
        max_num = 2**31 - 1
        min_num = -1 - max_num
        num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '+']
        num_str = ''
        flag = False
        for i in range(len(s)):
            if flag:
                if s[i] in num_list[:-2]:
                    num_str += s[i]
                else:
                    break
            if not flag:
                if s[i] in num_list[:-3] + num_list[-2:]:
                    flag = True   # flag为True将不再接受负号
                    num_str += s[i]
                elif s[i] == '0':
                    continue
                else:
                    break

        if not flag or num_str in num_list[-2:]:
            s = 0
            
        else:
            s = eval(num_str)
            if s > max_num:
                s = max_num
            elif s < min_num:
                s = min_num
        return s

if __name__ == '__main__':
    string = '00012'
    s = Solution()
    r = s.myAtoi(string)
    print(r)



