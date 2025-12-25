s="abcddabcdedf"
win=set()
left=0
right=0
st=0
max_len=0
for i in range(len(s)):
    while s[i] in win:
        win.remove(s[left])
        left+=1
    win.add(s[i])
    
    if i-left+1>max_len:
        max_len=i-left+1
        st=left
print(s[st:st+max_len])
    