import sys

m, n = map(int, sys.stdin.readline().split())
snacks = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(snacks)
result = 0 
while start<=end:
    distance = 0 
    mid = (start+end)//2
        
    if mid ==0:
        result = 0 
        break

    for snack in snacks:
        if snack>=mid:
            distance+=(snack//mid)
    
    if distance >= m:
        start = mid+1 
        result = mid 
    else:
        end = mid-1

print(result)