int romanToInt(char* s) {
    int arr[16];
    int i;
    for(i=0;s[i]!='\0';i++){
        switch(s[i]){
            case 'I':arr[i]=1;
                break;
            case 'V':arr[i]=5;
                break;
            case 'X':arr[i]=10;
                break;
            case 'L':arr[i]=50;
                break;
            case 'C':arr[i]=100;
                break;
            case 'D':arr[i]=500;
                break;
            case 'M':arr[i]=1000;
                break;
            default:arr[i]=0;
        }
    
    }
    i--;
    int sum=arr[i];
    for(int y=i;y-1>=0;y--){
        if(arr[y-1]<arr[y])
            sum-=arr[y-1];
        else
            sum+=arr[y-1];
    }
   return sum; 
}