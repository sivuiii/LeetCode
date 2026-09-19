class Solution:
    
    def validMountainArray(self, arr: list[int]) -> bool:
        
        f = 0
        
        for i in range(len(arr)-1) :
            if arr[i+1] > arr[i] :
                if f == 0 or f == 1:
                    f = 1
                else :
                    return False
            elif arr[i+1] < arr[i] :
                if f == 1 or f == 2:
                    f = 2
                else :
                    return False
            else :
                return False
        if f == 2 :
            return True
        else :
            return False
                    


        