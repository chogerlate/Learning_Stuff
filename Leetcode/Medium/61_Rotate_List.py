# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       
        traveller = head
        length = 1

        if head :
            traveller = head
            while traveller.next != None:
                length += 1
                traveller = traveller.next
            traveller.next = head # make our linked list become circular linked list

            k = k%length # k after we delete all unnessescery loops
            i = 0 # iter

            traveller = head
            while i != length-k-1 :
                traveller = traveller.next
                i += 1
            answer = traveller.next
            traveller.next = None

            return answer

        return head


