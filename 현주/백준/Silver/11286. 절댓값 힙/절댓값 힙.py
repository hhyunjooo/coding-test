import heapq
import sys
heap=[]

n=int(input())
for _ in range(n):
    x=int(sys.stdin.readline())
    if x!=0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if len(heap)!=0:
            result=heapq.heappop(heap)[1]
            print(result)
        else:
            print(0)