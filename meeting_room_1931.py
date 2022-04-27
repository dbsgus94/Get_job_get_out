import sys
input = sys.stdin.readline

N = int(input())
time = []
for _ in range(N):
    start_time, end_time = map(int,input().split())
    time.append([start_time,end_time])

time = sorted(time, key=lambda time: time[0])
time = sorted(time, key=lambda time: time[1])

last_time = 0 
result = 0 

for start,end in time:
    if start >=last_time:
        last_time = end
        result+=1 

print(result)
    