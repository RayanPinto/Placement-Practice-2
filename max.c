#include<stdio.h>
#include<stdlib.h>
int max(const void *a,const void * b){
    return (*( int*)a-*(int*)b);
}
int main(){
    int n;
    printf("Enter the number");
    
    scanf("%d",&n);
    int arr[n];
    printf("Enter the array elements");
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    qsort(arr,n,sizeof(int),max);
     for(int i=0;i<n;i++){
        printf("%d\t",arr[i]);
    }  
    return 0; 
}
