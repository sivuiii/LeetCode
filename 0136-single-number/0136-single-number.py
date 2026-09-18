class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums)> (3 * 10 ** 4):
            return 0
        elif len(nums) == 1:
            return nums[0] 

        nums.sort()

        for i in range(1,len(nums)-2):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]
        if nums[0] != nums[1]:
            return nums[0]
        elif nums[len(nums)-1] != nums[len(nums)-2]:
            return nums[len(nums)-1]