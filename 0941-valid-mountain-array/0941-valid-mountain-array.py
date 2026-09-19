class Solution:
    
    def validMountainArray(self, arr: list[int]) -> bool:
        
        inc = 0
        dec = 0
        
        for i in range(len(arr)-1) :
            if arr[i+1] > arr[i] :
                if dec == 0:
                    inc = 1
                else :
                    return False
            elif arr[i+1] < arr[i] :
                if inc == 1 :
                    dec = 1
                else :
                    return False
            else :
                return False
        if inc == 1 and dec == 1 :
            return True
        else :
            return False
                    


        