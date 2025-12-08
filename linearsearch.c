#include<stdio.h>
int main(){
    int arr[]={1,5,4,3,2};
    int key=2;
    int n=sizeof(arr)/sizeof(arr[0]);
    for(int i=0;i<n;i++){
        if(arr[i]==key){
            printf("%d",i);
        }
    }
    return 0;
}