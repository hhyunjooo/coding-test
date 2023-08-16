n=int(input())
list=[]
answer=[]
for _ in range(n):
    weight, height=map(int, input().split())
    list.append([weight, height])

for i in range(n):
    count=1
    for j in range(n):
        if list[i][0]<list[j][0] and list[i][1]<list[j][1]:
            count+=1
    answer.append(count)

for d in answer:
    print(d, end=' ')