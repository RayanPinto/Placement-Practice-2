arr=[4348,4832,34,5,3,45]
def mergesort(arr):
    n=len(arr)
    if n<=1:
        return arr
    mid=n//2
    left=mergesort(arr[:mid])
    right=mergesort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    i=j=0
    res=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    print(res)
    res.extend(left[i:])
    res.extend(right[j:])
    print(res)
mergesort(arr)