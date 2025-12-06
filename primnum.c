#include<stdio.h>
int isprime(int n){
    if(n<=1){
        return 0;
    }
    for(int i=2;i*i<=n;i++){
        if(n%i==0){
            return 0;
        }
    }
    return 1;
}
int main(){
    int n;
    printf("Enter a number");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        if(isprime(i)&& isprime(i+2)){
            printf("{%d\t%d}\n",i,i+2);
        }
    }

    return 0;
}