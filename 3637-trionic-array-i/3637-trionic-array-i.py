class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        f = 0
        
        for i in range(len(nums)-1) :
            if nums[i+1] > nums[i] :
                if f == 0 or f == 1:
                    f = 1
                elif f == 2 or f == 3:
                    f = 3
                else :
                    return False
            elif nums[i+1] < nums[i] :
                if f == 1 or f == 2:
                    f = 2
                else :
                    return False
            else :
                return False
        if f == 3 :
            return True
        else :
            return False

