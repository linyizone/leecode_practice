class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        temp = ""
        len_all = []
        for i in s:
            if i not in temp:
                temp += i
            else:
                len_all.append(len(temp))
                temp = temp.split(i)[-1] + i
        len_all.append(len(temp))
        return max(len_all)