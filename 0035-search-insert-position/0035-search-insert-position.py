class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        try :
            return nums.index(target)
        except :
            for i in range(1,10000) :
                try :
                    return nums.index(target+i)
                except :
                    continue
        return(len(nums))
