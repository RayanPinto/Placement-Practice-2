arr=[1,2,3,4,5]
n=len(arr)

count=0
for i in range(n):
    if arr[i]%2!=0:
        for j in range(i,n):
            sum=0
            sum+=arr[j]
            if sum%2==0:
                count+=1
print(count)

