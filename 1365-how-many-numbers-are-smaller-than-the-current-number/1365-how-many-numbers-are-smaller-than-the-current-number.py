class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr =[]
        num = sorted(nums)
        for i in range (0, len(nums)):
            arr.append(num.index(nums[i]))
        return arr