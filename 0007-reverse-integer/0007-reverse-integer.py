class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        neg = False
        if x<0:
            x = abs(x)
            neg = True
        while x!=0:
            y = y*10 + x%10
            x = x//10
        if neg == True:
            y *= -1
        if y < -(2 ** 31) or y > (2 ** 31)-1 :
            y = 0
        return y
        
        