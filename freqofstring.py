s="abcabcbabc"
l=len(s)
freq={}
res=[]
for i in range(l):
    ch=s[i]
    count=freq.get(ch,0)
    res.append(count)
    count=count+1
    freq[s[i]]=count
print(freq)
print(res)

