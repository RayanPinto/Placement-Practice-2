s="bbabcbcab"
def palindrome(s,low,high):
    if low>high:
        return 0
    if low==high:
        return 1
    if s[low]==s[high]:
        print(s[low],s[high])
        return palindrome(s,low+1,high-1)+2
    return max(palindrome(s,low,high-1),palindrome(s,low+1,high))
print(palindrome(s,0,len(s)-1))