class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr =[]
        for val in range(1, len(nums), 2):
            freq = nums[val - 1]
            arr += [nums[val]] * freq
        return arr
    