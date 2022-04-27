import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
parrot = [deque(input().rstrip().split()) for _ in range(N)]

L = input().rstrip().split()
Removed = []
for word in L:
    for i in range(N):
        if parrot[i] and word == parrot[i][0]:
            parrot[i].popleft()
            Removed.append(word)
            
for i in range(N):
    if parrot[i]:
        print("Impossible")
        #시간 단축 꿀팁 
        exit()
        
if L != Removed:
    print("Impossible")
else:
    print("Possible")