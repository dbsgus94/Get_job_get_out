# 플로이드 워셜 알고리즘

INF = int(1e9)

n = int(input()) # 노드 수
m = int(input()) # 간선 수

graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 리스트 초기화 (무한)

for a in range(1,n+1):
    for b in range(1, n+1):
        if a==b :
            graph[a][b] = 0 # 자기 자신에게로 가는 거리는 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c # a에서 b로 가는 거리는 c (이웃하는 노드 정보 모두 저장)

# 플로이드 워셜 알고리즘
for k in range(1, n+1): # 중간 노드로 삼을 노드
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b]) # 현재 저장된 거리보다 k 거쳐 가는 게 짧으면 업데이트됨


# 모든 노드에 대한 최단거리 matrix가 프린트됨
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()