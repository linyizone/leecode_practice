'''
输入：
nums1 = [4, 5, 7, 10, 0, 0, 0]
length1 = 4

nums2 = [3, 6, 11]
length2 = 3

输出：
[3, 4, 5, 6, 7, 10, 11]
'''

# def solution(x, y):
#     while 0 in x:
#         x.remove(0)
#     while 0 in y:
#         y.remove(0)   
#     z = x + y
#     z.sort()
#     return z
# nums1 = [4, 5, 7, 10, 0, 0, 0]
# nums2 = [3, 6, 11]

# print(solution(nums1, nums2))

# def solution(x, y):
#     tmp = 99
#     for i in x:
#         if 

# def solution(x, y):
#     len1 = len(x)
#     len2 = len(y)
#     for i in range(len1):
#         if x[i] == 0:
#             x[i] = 99
#         if x[i] > y[0]:
#             x[i], y[0] = y[0], x[i]
#             for j in range(len2-1):
#                 if y[j] > y[j+1]:
#                     y[j], y[j+1] = y[j+1], y[j]
#                 else:
#                     break
#     return x

def solution(x, y, len1, len2):
    l1 = len(x)
    l2 = len(y)
    n = 1
    m = 1

    if x[0] < y[0]:
        pass
    else:
        x[0], y[0] = y[0], x[0]
    for i in range(l1-1, 0, -1):
        print(len1 - n, len2 - m)
        if x[len1 - n] > y[len2 - m]:
            x[i] = x[len1 - n]
            n += 1
        else:
            x[i] = y[len2 - m]
            m += 1
    return x

nums1 = [4, 5, 7, 10, 0, 0, 0]
nums2 = [3, 6, 11]
len1 = 4
len2 = 3
#print(solution(nums1, nums2))
print(solution(nums1, nums2, len1, len2))
