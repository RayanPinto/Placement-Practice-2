#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(){
    char str[]="abcdabcde";
    int n=strlen(str);
    int max_len=0;
    
    for(int i=0;i<n;i++){
        int count=1;
        int freq[256]={0};
        for(int j=i;j<n;j++){
            if(freq[(unsigned char)str[j]]==1){
                break;
            }
        
        freq[(unsigned char)str[j]]=1;
        count++;
        if (count > max_len) {
                max_len = count;
            }
        }

    }
    printf("Longest substring length = %d\n", max_len);
    
    return 0;
    return 0;
}