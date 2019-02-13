root = [1, 2, 3, -1, 4, 5, 6]

def solution(root):
    l = len(root)-1
    pos = 0
    rslt = [root[pos]]
    stack_doing = [pos]
    stack_done = []
    while 0 not in stack_done:
        time.sleep(1)
        print(pos)   
        print(stack_doing)
        print(stack_done)
        if pos*2+1<=l and root[pos*2+1]!=-1 and pos*2+1 not in stack_done:
            pos = pos*2 + 1
            stack_doing.append(pos)
            rslt.append(root[pos])
        elif pos*2+2<=l and root[pos*2+2]!=-1 and pos*2+2 not in stack_done:
            pos = pos*2 + 2
            stack_doing.append(pos)
            rslt.append(root[pos])
        else:
            stack_done.append(stack_doing[-1])
            stack_doing.remove(stack_doing[-1])
            if stack_doing != []:
                pos = stack_doing[-1]           
    return rslt
print(solution(root))