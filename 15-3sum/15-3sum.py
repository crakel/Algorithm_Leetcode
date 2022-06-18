from itertools import combinations
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()
        # 투 포인터 풀이
        for i in range(len(nums) - 2):
            # 중복 skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums)-1
            
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                
                if s == 0:
                    answer.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                
                elif s < 0:
                    left += 1
                
                else:
                    right -= 1
                    
        return answer
        # combination 완탐 -> 메모리 초과
        # for c in list(combinations(nums, 3)):
        #     if sum(c) == 0 and c not in answer:
        #         answer.append(c)
        # return answer