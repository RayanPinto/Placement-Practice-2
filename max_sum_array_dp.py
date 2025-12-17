arr=[-10,3,4,32,1,2,-1]
n=len(arr)
dp=[0]*(n+1)
current_sum=0
max_sum=0
dp[0]=arr[0]
for i in range(n):
    current_sum=max(current_sum+arr[i],arr[i])
    max_sum=max(current_sum,max_sum)
print(max_sum)