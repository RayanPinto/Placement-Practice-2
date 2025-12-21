a="abcdjkk"
b="ffskabcd"
def lcs(s1,s2,n,m):
    if(n<0 or m<0):
        return 0
    if(s1[n]==s2[m]):
        return 1+lcs(s1,s2,n-1,m-1)
    return max(lcs(s1,s2,n-1,m),lcs(s1,s2,n,m-1))
print(lcs(a,b,len(a)-1,len(b)-1))