count = int(input())
height_list = []
for i in range(count):
    height_list.append(int(input()))

result = 0
s = []
print("height_list is ", height_list)
for i in range(count):
    print("     index is ", i, "s is ", s)
    while s and height_list[s[-1]] > height_list[i]: #스택 마지막 높이, 현재 인덱스의 높이를 비교
        print("before s is ", s)
        height = height_list[s[-1]]
        s.pop()
        width = i
        if s:
            width = (i - s[-1] -1)
            print("after s is ", s, "height is", height, "width is ", width, "넓이는 ", (i - s[-1] -1))
        result = max(result, width * height)
    s.append(i) #막대 인덱스 넣음

while s:
    height = height_list[s[-1]]
    s.pop()
    width = count
    if s:
        width = (count - s[-1] - 1)
    result = max(result, width * height)
    
print(result)
