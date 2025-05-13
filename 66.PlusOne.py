# 66. Plus One
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # # write the code step by step
        # for i in range(len(digits) - 1):
        #     if digits[i] == 9:
        #         digits[i] = 0
        #     else:
        #         digits[i] += 1
        #         return digits
        # write in one line
        return list(map(int, str(int(''.join(map(str, digits))) + 1)))
        # 1.	map(str, digits) ：把数字转成字符串。
        # 2.	''.join(...) ：拼成一个大整数的字符串。
        # 3.	int(...) + 1 ：整体转成整数加 1。
        # 4.	再用 str(...) 和 map(int, ...) 把每一位拆回数组。
        # 5.	最后 list(...) 转成列表返回。
solution = Solution()
print(solution.plusOne([1,2,9]))