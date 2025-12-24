def max_score(a,p):
    n=len(a)
    score=0
    for i in range(n):
        diff=a[i]-p[i]
        if diff>0:
            score+=diff
    return score




A = [10, 5, 8, 7]
P = [3, 6, 9, 1]

print(max_score(A, P))  