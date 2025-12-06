def two_sum(arr,key):
    seen={}
    for i,j in enumerate(arr):
        diff=key-j
        if diff in seen:
            return [seen[diff],i]
        seen[j]=i
    return None
print(two_sum([2,7,7,2],9))