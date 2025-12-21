arr=[1,4,2,3,5,5,4,1]
n=len(arr)
from collections import Counter
arr1=Counter(arr)
print(arr1)
for i in arr1:
    if arr1[i]==1:
        print(i)

    
