# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if l1==None and l2!=None:
            return l2
        elif l2==None and l1!=None:
            return l1
        elif l1==None and l2==None:
            return None
        list1 = []
        while l1!=None:
            list1.append(l1.val)
            l1 = l1.next
        list2 = []
        while l2!=None:
            list2.append(l2.val)
            l2 = l2.next
        len1 = len(list1)
        len2 = len(list2)
        l_d = [0] * (max(len1, len2)-min(len1, len2))
        if min(len1, len2)==len1:
            list1.extend(l_d)
        else:
            list2.extend(l_d)
        l3 = []
        up = 0
        for i in range(max(len1, len2)):
            f1 = (list1[i] + list2[i] + up) % 10
            f2 = (list1[i] + list2[i] + up) // 10
            up = f2
            l3.append(f1)
            if list1[i]+list2[i]>9:
                up = 1
        if up==1:
            l3.append(1)
        return l3

class Solution2:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if l1==None and l2!=None:
            return l2
        elif l2==None and l1!=None:
            return l1
        elif l1==None and l2==None:
            return None
        num1 = 0
        count = 1
        while l1!=None:
            num1 = num1 + l1.val*count
            count *= 10
            l1 = l1.next
        num2 = 0
        count = 1
        while l2!=None:
            num2 = num2 + l2.val*count
            count *= 10
            l2 = l2.next
        num3 = num1 + num2
        num3 = str(num3)
        len3 = len(num3)
        l3 = []
        for i in range(len3-1, -1, -1):
            l3.append(int(num3[i]))
        return l3