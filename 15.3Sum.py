# 15.3Sum
# 这个是2sum的进阶版，思路是用两个指针，一个头指针一个尾部指针
# 依次向后向前移动。
# 如果和小于零，就移动头指针（前提是要先sort数组）
# 这样在两个指针相遇之前救能找到符合的组合
from typing import List

class Solution:    
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        # using the two pointers
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1          # from the start to end
            k = len(nums) - 1  # from the end to start

            while j < k: # if j > k which means the pointer meet
                sum = nums[i] + nums[j] + nums[k]

                if sum < 0: # it means the sum is smaller so move the low pointer
                    j += 1
                elif sum > 0:
                    k -= 1 # move the high pointer
                else:
                    result.append([nums[i] , nums[j] , nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return result

nums = [1, 2, 3, 4, -1, -1, -2, -5]
solution = Solution()  
result = solution.threeSum(nums)
print(result)