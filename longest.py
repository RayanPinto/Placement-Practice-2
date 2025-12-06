def long(arr=[1,-1,5,-2,3],k=3):
    best=0
    prefix=0
    seen={0:-1}
    for i,j in enumerate(arr):
        prefix+=j
        