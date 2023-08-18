from collections import deque
n, m ,v = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m): # 간선 개수만큼 그래프 생성
    a,b=map(int,input().split())
    graph[a]+=[b] # a에 b 연결
    graph[b]+=[a] # b에 a 연결 -> 양방향, 원래꺼에 합쳐짐

#dfs 깊이
visited=[0]*(n+1) # 방문한 컴퓨터인지 표시, 1번 컴퓨터가 1번 인덱스s
for j in range(1, n+1):
    graph[j].sort()
def dfs(v):
    print(v, end=" ")
    visited[v]=1
    for nx in graph[v]:
        if visited[nx]==0:
            dfs(nx)
dfs(v)
print()

#bfs
visited=[0]*(n+1)

def bfs(start):
    q = deque([start])#넣은수부터 들어감
    visited[start] = 1
    
    while q:
        node = q.popleft()
        print(node, end=" ")
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = 1
        
bfs(v)