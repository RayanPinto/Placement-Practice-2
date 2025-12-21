freq={}
arr=[1,5,3,2,1,3,3]
count=0
for i in range(len(arr)):
    ch=arr[i]
    count=freq.get(ch,0)
    count=count+1
    freq[arr[i]]=count
print(freq)