# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        answer = [ ListNode("") for i in range(k)] # making answer list from given k splits
        pointer = head

        # meansure the length of given linkedlist
        length = 0 
        while pointer != None :
            length += 1
            pointer = pointer.next
        
        if length == 0 :
            return answer
        elif length <= k :
            index = 0 
            pointer = head
            while pointer != None :
                answer[index].val = pointer.val
                index += 1
                pointer = pointer.next
        else:
            index = 0
            pointer = head
            avg_len = length//k
            remain = length - avg_len*k
            each_len = [ avg_len for i in range(k) ]
            for i in range(remain):
                each_len[i] += 1
            for sub_len in each_len:
                cur = answer[index]
                for i in range(sub_len):
                    cur.val = pointer.val
                    pointer = pointer.next
                    if i < sub_len-1  :
                        cur.next = ListNode("")
                        cur = cur.next
                index += 1

        return answer