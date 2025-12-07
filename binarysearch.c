#include<stdio.h>
int binarys(int arr[],int st,int end,int key){
    if(st<=end){
        int mid=(st+end)/2;
        if(arr[mid]==key){
            return mid;
        }else if(arr[mid]<key){
            return binarys(arr,mid+1,end,key);
        }else{
            return binarys(arr,st,mid-1,key);
        }
    }
    return -1;
}
int main(){
    int arr[]={1,2,3,4,5};
    int n=sizeof(arr)/sizeof(arr[0]);
    int val=binarys(arr,0,n-1,2);
    printf("%d\t",val);
    return 0;
}