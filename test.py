def solution(l1, l2):
    if l1==[]:
        return l2
    elif l2==[]:
        return l1
    elif l1==[] and l2==[]:
        return []
    len1 = len(l1)
    len2 = len(l2)
    l_d = [0] * (max(len1, len2)-min(len1, len2))
    if min(len1, len2)==len1:
        l1.extend(l_d)
    else:
        l2.extend(l_d)
    l3 = []
    up = 0
    for i in range(max(len1, len2)):
        f1 = (l1[i] + l2[i] + up) % 10
        f2 = (l1[i] + l2[i] + up) // 10
        up = f2
        l3.append(f1)
        if l1[i]+l2[i]>9:
            up = 1
    if up==1:
        l3.append(1)
    return l3

l1 = [2, 4, 3]
l2 = [5, 6, 4]
print(solution(l1, l2))
