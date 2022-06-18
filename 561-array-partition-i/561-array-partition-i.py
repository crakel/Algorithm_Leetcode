class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 슬라이싱 풀이
        return sum(sorted(nums)[::2])
        # nums.sort()
        # answer = 0
        # for i in range(0, len(nums), 2):
        #     answer += nums[i]
        # return answer