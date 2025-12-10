arr="aeiou"
arr1="rayan"
count=0
for i in range(len(arr1)):
    if arr1[i] in arr:
        count=count+1
print(count)