#노드(컴퓨터) 수 
n = int(input())
#엣지(네트워크) 수 
m = int(input())

graph = [[] for _ in range(n+1)] 

#그래프 생성 
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) 

visited = [False]*(n+1)
result = 0
def dfs(graph,v,visited):
    global result 
    visited[v] = True 
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            result +=1 

dfs(graph,1,visited) 
print(result)
            
            