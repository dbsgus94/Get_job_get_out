computer_count = int(input())
network_count = int(input())

graph = [[] for _ in range(computer_count + 1)]
for i in range(network_count):
    from_com, to_com = map(int, input().split())
    graph[from_com].append(to_com)
    graph[to_com].append(from_com)
#graph = [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

start_com = 1
linked_with_start_com = []


def dfs(com_num):
    linked_com_list = []
    for linked_com in graph[com_num]:
        if linked_com is start_com or linked_com in linked_with_start_com:
            continue
        else:
            linked_with_start_com.append(linked_com)
            linked_com_list.append(linked_com)
    # print('this com is ', com_num)
    # print('linked_with_start_com is ', linked_with_start_com)
    
    for com in linked_com_list:
        dfs(com)

dfs(start_com)
print(len(linked_with_start_com))
# print(linked_with_start_com)