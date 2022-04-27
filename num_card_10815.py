n = int(input())
card = list(map(int,input().split()))
m = int(input())
target_card = list(map(int,input().split()))

card.sort()

def binary_search(data,start,end,target):
    while start<=end:
        mid = (start+end)//2 
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1 
        else:
            start = mid+1 
    return None 

result = []
for i in range(m):
    if binary_search(card,0,n-1,target_card[i]) == None:
        result.append(0)
    else:
        result.append(1)
    print(result[i],end=' ')
    
