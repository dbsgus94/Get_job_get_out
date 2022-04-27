# [
#     'So when I die (the [first] I will see in (heaven) is a score list).', 
#     '[ first in ] ( first out ).', 
#     'Half Moon tonight (At least it is better than no Moon at all].', 
#     'A rope may form )( a trail in a maze.', 
#     'Help( I[m being held prisoner in a fortune cookie factory)].', 
#     '([ (([( [ ] ) ( ) (( ))] )) ]).', 
#     ' .'
# ]
while True:
    sentence = input()
    stk = []
    temp = True
    
    if sentence == '.':
        break
 
    for word in sentence:
        if word == '(' or word == '[':
            stk.append(word)
        elif word == ')':
            if not stk or stk[-1] == '[':
                temp = False
                break
            elif stk[-1] == '(':
                stk.pop()
        elif word == ']':
            if not stk or stk[-1] == '(':
                temp = False
                break
            elif stk[-1] == '[':
                stk.pop()

    if temp and not stk:
        print('yes')
    else:
        print('no')
        