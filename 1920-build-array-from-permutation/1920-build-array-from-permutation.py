class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range (0, n):
             result.append(nums[nums[i]])
        return result
        