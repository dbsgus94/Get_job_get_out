import sys
input = sys.stdin.readline 

while True:
    sentence = input().rstrip()
    if sentence == ".":
        break 
    
    word_stack = []
    for word in sentence:
        if word == "[" or word =="(":
            word_stack.append(word) 
        elif word =="]":
            if word_stack and word_stack[-1] == "[":
                word_stack.pop()
            else:
                word_stack.append(word)
                break 
        elif word == ")":
            if word_stack and word_stack[-1] == "(":
                word_stack.pop()
            else:
                word_stack.append(word)
                break 

    if word_stack:
        print("no")
    else:
        print("yes")

