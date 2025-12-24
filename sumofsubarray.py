def func(arr):
    n=len(arr)
    total=0
    mod=10**9+7
    for i in range(n):
        contrib=arr[i]*(i+1)*(n-i)
        total=(total+contrib)
    return total
print(func([1,2,3]))