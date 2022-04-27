from collections import deque

bird_count = int(input())
bird_sentence_list = list()
#[
#   deque(['i', 'want', 'to', 'see', 'you']), 
#   deque(['next', 'week']), 
#   deque(['good', 'luck'])
# ]
for i in range(bird_count):
    bird_sentence_list.append(deque(map(str, input().split())))
# print("sentence list is ", bird_sentence_list)
sentence = deque(map(str, input().split()))

def possible(sentence, arr):
    misscount = 0
    j = 0
    while sentence: #내가 받아적은 문장이 끝날때까지
        if arr[j] and sentence[0] == arr[j][0]: #앵무새 첫 문장 남아있고 and 내 문장 첫 단어와 앵무새 첫 문장 첫 단어가 같다면
            print("if", "bird is", j)
            print("bird sentencs is ", arr[j], "first is ", arr[j][0], "!!!")
            print("my sentence is", sentence, "and first word is ", sentence[0])
            arr[j].popleft()
            sentence.popleft()
            misscount = 0 #맞은 경우가 나왔으면 다시 처음부터 세기 위해 0으로 변경해준다.
            print("array is", arr)
            print('')
        else:
            print("else", "bird is", j)
            print("bird sentencs is ", arr[j])
            print("my sentence is", sentence, "and first word is ", sentence[0])
            # print('ㅡ')
            if misscount == bird_count:
                return False
            misscount += 1 #새의 문장 첫 단어와 내 첫 단어가 안 맞는다면 잘못된 경우리므로 +1
            print("miscount is ", misscount)
            print('')
        j = (j + 1) % bird_count

    empty = 0
    for i in range(bird_count): #앵무새들이 들은 문장을 다 사용했는지 확인
        if len(arr[i]) == 0:
            empty += 1

    if not sentence and empty == bird_count: #내가 적은 문장이 false 즉, 다 사용했고, 앵무새들의 문장도 다 사용했다면
        return True
    else:
        return False


if possible(sentence, bird_sentence_list):
    print("Possible")
else:
    print("Impossible")
    