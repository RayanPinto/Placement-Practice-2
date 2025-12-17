n=1034
print(type(n))
sum=0
d=str(n)
for i in range(len(d)):
    r=n%10
    sum+=r
    n=n//10
print(sum)