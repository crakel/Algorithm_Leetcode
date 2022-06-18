import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        left = []
        right = []
        
        cur = 1
        for i in range(len(nums)):
            left.append(cur)
            cur *= nums[i]
        
        cur = 1
        for i in range(len(nums)-1, -1, -1):
            right.append(cur)
            cur *= nums[i]
        

        for i in range(len(nums)):
            answer.append(left[i]*right[-i-1])
        
        # 시간초과
        # for i in range(len(nums)):
        #     answer.append(math.prod(nums[:i]) * math.prod(nums[i+1:len(nums)]))
        return answer