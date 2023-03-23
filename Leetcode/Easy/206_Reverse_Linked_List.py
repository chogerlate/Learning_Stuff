# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        save_data = [] 
        cur = head

        if not head :
            return head
        while cur != None:
            save_data.append(cur.val)
            cur = cur.next
        
        print(save_data)
        cur = head
        while cur != None:
            cur.val = save_data.pop()
            cur = cur.next

        return head 