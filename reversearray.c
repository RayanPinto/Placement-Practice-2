#include<stdio.h>
int main(){
    int arr[]={1,2,3,4,5};
    int n=sizeof(arr)/sizeof(arr[0]);
    int i=0;
    int j=n-1;
    while(i<j){
        arr[i]^=arr[j];
        arr[j]^=arr[i];
        arr[i]^=arr[j];
        i++;
        j--;
    }
    printf("The reversed array is");
    for(int i=0;i<n;i++){
        printf("%d\t",arr[i]);
    }
    return 0;
}