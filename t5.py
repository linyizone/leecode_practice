#root = [1, 2, 3, -1, 4, 5, 6]

def solution(root, v1, v2):
    a = root.index(v1)
    b = root.index(v2)
    if v1<v2:
        small = v1
        big = v2
    else:
        small = v2
        big = v1
    ans = [small]
    while small != 0:
        if small%2==0:
            small = (small - 2) / 2
            ans.append(small)
        else:
            small = (small - 1) / 2
            ans.append(small)
    while big not in ans:
        if big%2==0:
            big = (big - 2) / 2
        else:
            big = (big - 1) / 2
    return root[int(big)]
root = [1, 2, 3, -1, 4, 5, 6]
print(solution(root, 5, 6))
# 如果用__dict__可以打印所有属性
    