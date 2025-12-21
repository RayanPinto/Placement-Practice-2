a="forgeeksskeegfor"
from functools import lru_cache
@lru_cache(None)


def lps(a,n,m):
    if m==n:
        return 1
    if n>m:
        return 0
    if (a[n]==a[m]):
        return 2+lps(a,n+1,m-1)
    return max(lps(a,n+1,m),lps(a,n,m-1))







print(lps(a,0,len(a)-1))