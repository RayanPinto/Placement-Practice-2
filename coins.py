arr=[1,2,5]
tar=3
def coins(arr,tar):
    n=len(arr)
    dp=[float('inf')]*(tar+1)
    dp[0]=0
    for coin in arr:
        for j in range(coin,tar+1):
            dp[j]=min(dp[j],dp[j-coin]+1)
    return dp[3]
print(coins(arr,tar))
