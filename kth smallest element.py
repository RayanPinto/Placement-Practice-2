from collections import Counter
arr=[4,1,2,2,3,1,5]
k=2
arr1=Counter(arr)
def kth(arr1,k):
    uniq=[x for x in arr1 if arr1[x]==1]
    print(uniq)
    if k<=len(uniq):
        print(uniq[k-1])
kth(arr1,2)
