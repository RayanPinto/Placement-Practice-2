s="AGGTAB"
s1="GXTXAYB"
n=len(s)
m=len(s1)
def lcs(s,s1,n,m):
    
    if m==0 or n==0:
        return 0
    if s[n-1]==s1[m-1]:
        return 1+lcs(s,s1,n-1,m-1)
    return max(lcs(s,s1,n-1,m),lcs(s,s1,n,m-1))
print(lcs(s,s1,n,m))