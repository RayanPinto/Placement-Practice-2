arr=[1,43,4,5,6,5,8]

print(arr)
def quicksort(arr):
    n=len(arr)
    if n<=1:
        return arr
    mid=arr[n//2]
    left=[x for x in arr if x<mid]
    right=[x for x in arr if x>mid]
    middle=[x for x in arr if x==mid]
    
    return quicksort(left)+middle+quicksort(right)
print(quicksort(arr))

