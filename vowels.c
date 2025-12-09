#include<stdio.h>
#include<ctype.h>
#include<string.h>
int countvowel(char *s,int *v,int *c){
    char ss[256]={0};
     *v=0;
    *c=0;
    int n=strlen(s);
    int i=0;
    while(s[i]!='\0'){
        s[i]=tolower(s[i]);
        i++;
    }
    int j=0;
    for(int i=0;i<n;i++){
        if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'){
            (*v)++;
            ss[j]=s[i];
            j++;
        }else{
            (*c)++;
        }
    }
    printf("%s",ss);
    return 0;
}
int main(){
    char s[]="Abcdddaeiou";
    int v,c;
    countvowel(s,&v,&c);
    printf("%d\t%d\t",v,c);
    return 0;

}