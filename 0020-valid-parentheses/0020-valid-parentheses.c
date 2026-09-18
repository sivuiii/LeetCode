bool isValid(char* s) {
    char stack[5002];
    int n=0;
    
    for(int i=0;i<strlen(s);i++){
        if(s[i]=='('||s[i]=='['||s[i]=='{'){
            stack[n]=s[i];
            n++;
        }else if(n==0){
            return false;
        }else if(stack[n-1]=='('&&s[i]==')'||
                 stack[n-1]=='{'&&s[i]=='}'||
                 stack[n-1]=='['&&s[i]==']'){
            n--;
            stack[n]='\0';
        }
        else{
            return false;}
        
        if(strlen(stack)==5001)
            {return false;}
    }
    if(strlen(stack)!=0)
        return false;
    else
        return true;
}