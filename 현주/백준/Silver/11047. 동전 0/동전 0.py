import sys
n, k=map(int, input().split()) #n종류, 합이 k
A=[]
for _ in range(n):
    A.append(int(input()))

A.sort(reverse=True)
count=0
for i in range(n):
    count += k//A[i]
    k=k%A[i]

print(count)