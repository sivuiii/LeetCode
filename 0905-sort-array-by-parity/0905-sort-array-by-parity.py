class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        odd = []
        for i in range(len(nums)-1) :
            if nums[i] % 2 != 0 :
                odd.append(nums[i])
        for i in range(len(odd)) :
            nums.append(odd[i])
            nums.pop(nums.index(odd[i]))
        return nums