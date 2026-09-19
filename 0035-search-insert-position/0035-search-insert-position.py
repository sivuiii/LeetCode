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

        # si, ei = 0, len(nums)-1
        # while si <= ei :
        #     mi = (si+ei) // 2
        #     if nums[mi] == target :
        #         return mi
        #     elif nums[mi] < target :
        #         si = mi + 1
        #     else :
        #         ei = mi -1
        # return si
