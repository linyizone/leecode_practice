# x = [4, 5, 7, 10]
# rslt = 0
# for i in x:
#     for j in x:
#         if i==j:
#             pass
#         else:
#             if i+j==12:
#                 rslt = 1
#                 break

# print(rslt)

# def Twosum():
#     x = [4, 5, 7, 10]
#     for i in x:
#         for j in x:
#             if i==j:
#                 pass
#             else:
#                 if i+j==12:
#                     return True
#     return False

# print(Twosum())

# def Twosum():
#     x = [4, 5, 7, 10]
#     for i in x:
#         for j in x j = i+1:
#             if i+i+1==12:
#                 return True
#     return False

# print(Twosum())
# x = [4, 5, 7, 9]

# def Twosum(x, target):
#     y = set()
#     for i in x:
#         if target-i in y:
#             return  True
#         y.add(i)
#     return False

# print(Twosum(x, 8))

'''
输入1:
nums = [4, 5, 7, 10]
target = 12
输出1: True

输入2：
nums = [4, 5, 7, 10]
target = 8

输出: False
'''

x = [4, 5, 7, 9]

def Twosum(x, target):
    y = set()
    for i in x:
        if target-i in y:
            return  True
        y.add(i)
    return False

print(Twosum(x, 6))