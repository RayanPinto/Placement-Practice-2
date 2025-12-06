#include<stdio.h>
#include<string.h>
int main(){
   char str[]="abcabcadcb";
   int n=strlen(str);
   int st=0;
   int maxi=0;
   for(int i=0;i<n;i++){
    int freq[256]={0};
    int len=0;
    for(int j=i;j<n;j++){
        if(freq[(unsigned char)str[j]]==1){
            break;
        }
        freq[(unsigned char)str[j]]=1;
        len++;
         if (len>maxi){
        maxi=len;
        st=i;
    }
        
    }
   
   }
   for(int i=st;i<st+maxi;i++){
    printf("%c",str[i]);   }

    return 0;

}