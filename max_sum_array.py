arr=[1,4,5,6,7,1]
win=[]
winsum=0
maxsum=0
n=len(arr)
left=0
right=0
k=3
for i in range(n):
    if right-left==k:
        win.remove(arr[left])
        winsum-=arr[left]
        left+=1
    win.append(arr[i])
    print(win)
    right=right+1
    winsum+=arr[i]
    if winsum>maxsum:
        maxsum=winsum
print(maxsum)
