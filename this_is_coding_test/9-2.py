# 다익스트라 알고리즘 (priority queue)

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)] # 그래프 저장
distance = [INF] * (n+1) # 최단거리 테이블. node 별 최단 거리 업데이트를 위한 테이블 (0번째 인덱스는 버리는거)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = [] # queue

    heapq.heappush(q, (0,start)) # queue에 (거리, 노드) 넣음! (시작 node라서 거리 0)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # heap에 있는 것 중 가장 짧은 것 꺼내보기

        if distance[now]<dist: # 이미 저장되어 있는 distance가 더 짧으면 무시 (버림)
            continue

        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))