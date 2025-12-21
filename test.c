#include<stdio.h>
#include<stdlib.h>
int compare(const void *a,const void *b){
    int x=*(int *)a;
    int y=*(int *)b;
    if(x<y){
        return 1;
    }
    if(x>y){
        return -1;
    }
    return 0;
}
int main(){
    int arr[]={1,5,41,4,6,4,2};
    int n=sizeof(arr)/sizeof(arr[0]);
    qsort(arr,n,sizeof(int),compare);
    for(int i=0;i<n;i++){
        printf("%d\t",arr[i]);
    }
    return 0;
}