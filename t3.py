# 输入1：
# equation = "([][]{})"

# 输出1: true

# 输入2：
# equation = "([)]"

# 输出2：
# false

def solution(equ):
    sta = []
    for i in equ:
        if i == "(" or i == "[" or i == "{":
            sta.append(i)
            continue
        if sta == []:
            return False
        if i == ")" and sta[-1] != "(" or i == "}" and sta[-1] != "{" or i == "]" and sta[-1] != "[":
            return False
        else:
            sta.pop(-1)
    if sta != []:
        return False
    return True

equation1 = "([][]{})"
equation2 = ")))"
print(solution(equation1))
print(solution(equation2))