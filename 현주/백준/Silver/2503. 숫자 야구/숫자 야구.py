#동일한 위치: 스트라이크 1
#숫자는 맞는데 다른 위치: 볼 1
from itertools import combinations,permutations
number=['1', '2', '3', '4', '5', '6', '7', '8', '9']
question=int(input())
combi=list(permutations(number, 3))

for _ in range(question): #4번
    n, s, b=list(map(int, input().split())) #민혁 질문, 스트라이크, 볼
    n=list(str(n)) #1, 2, 3
    cnt=0

    for i in range(len(combi)): #조합 인덱스
        strike=ball=0
        i-=cnt
        for j in range(3):
            if combi[i][j]==n[j]:
                strike+=1
            elif n[j] in combi[i]:
                ball+=1
        if (strike != s) or (ball != b):
            combi.remove(combi[i])
            cnt+=1 #리스트 줄어들어도 index 벗어나지 않게
print(len(combi))