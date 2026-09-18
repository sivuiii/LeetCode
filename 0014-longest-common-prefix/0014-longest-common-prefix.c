char* longestCommonPrefix(char** strs, int strsSize) {
    char *c= malloc(200);;
    int j=0;
    if(strsSize<=1){
        return *strs;
    }
    for(int i=0;i<strsSize;i++){
        if(strs[i][j]!='\0'){
            if(strs[i][j]==strs[i+1][j]){
                c[j]=strs[i][j];
                
            }
            else{
                c[j]='\0';
                return c;}
        }else{
            c[j] = '\0';
            return c;
        }

        if(i==strsSize-2){
            i=-1;
            j++;
        }
    }
    c[j]='\0';
    return c;
}