class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        try :
            return nums.index(target)
        except :
            for i in range(1,999) :
                try :
                    return nums.index(target+i)
                except :
                    continue
        return(len(nums))
