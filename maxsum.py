arr=[1,3,4,2,1,2,3,4]
tar=6
n=len(arr)
right=0
left=0
win=[]
winsum=0
for i in range(n):
    
    winsum+=arr[i]
    right+=1
    while  winsum>tar:
        win.pop(0)
        winsum-=arr[left]
        left+=1
    win.append(arr[i])
    if winsum==tar:
        print(winsum)
        print(win)
        print(arr[left:i+1])
    