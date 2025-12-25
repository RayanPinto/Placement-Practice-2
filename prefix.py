seen={0:[-1]}
arr = [1, 3, 4, 2]
target = 4
prefix_sum=0
for i in range(len(arr)):
    prefix_sum+=arr[i]
    if prefix_sum-target in seen:
        for idx in seen[prefix_sum-target]:
            print(arr[idx+1:i+1])
    if prefix_sum in seen:
        seen[prefix_sum].append(i)
    else:
        seen[prefix_sum]=[i]
    