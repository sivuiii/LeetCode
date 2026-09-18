#include <math.h>
bool isPalindrome(int x) {
    if (x < 0)
        return false;

    if (x == 0)
        return true;

    int arr[10],y,n=0;
    while(x>0){
        arr[n]=x%10;
        x/=10;
        n++;
    }
    for(int i=0;i<n/2;i++){
        if(arr[i]!=arr[n-1-i])
            return false;
    }    
    
    return true;
}