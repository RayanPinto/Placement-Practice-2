tasks = [4, 2, 10, 3, 5]
k = 12
m = 1

import heapq
def task(tasks,k,m):
    battery_used=0
    max_heap=[]
    ct=0
    su=0
    for cost in tasks:
        battery_used+=cost
        heapq.heappush(max_heap,-cost)
        ct+=1
        if battery_used>k:
            if su<m and max_heap:
                maxcost=-heapq.heappop(max_heap)
                battery_used-=maxcost
                su+=1
            else:
                return ct-1
print(task(tasks,k,m))