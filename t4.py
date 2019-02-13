a = [0, 1, 1, 1, 1, 1]
import time
def solution(x):
    num = len(x)
    left = 0
    right = num - 1
    #while right-(right+left)//2>=1 and (right+left)//2-left>=1:
    while right-left>=2:
        time.sleep(1)
        print(left, right)
        if x[(right+left)//2] == 1:
            right = (right+left)//2
        else:
            left = (right+left)//2
    if x[left] == 0:
        return right
    else:
        return left

print(solution(a))
 