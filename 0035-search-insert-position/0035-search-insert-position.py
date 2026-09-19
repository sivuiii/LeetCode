class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        si, ei = 0, len(nums)-1
        while si <= ei :
            mi = (si+ei) // 2
            if nums[mi] == target :
                return mi
            elif nums[mi] < target :
                si = mi + 1
            else :
                ei = mi -1
        return si
