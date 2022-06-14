
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 딕셔너리 활용
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = i
        
        for i, num in enumerate(nums):
            if target - num in dic and i != dic[target-num]:
                return [i, dic[target-num]]
        
        # 완전탐색 7391 ms
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]