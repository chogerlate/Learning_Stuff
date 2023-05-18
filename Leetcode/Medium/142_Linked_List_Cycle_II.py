# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer = head # move 2 step at a time
        fast_pointer = head # move 1 step at a time
        
        while fast_pointer != None and slow_pointer != None :
            if fast_pointer == None or slow_pointer == None :
                return None
            if fast_pointer.next == None or fast_pointer.next.next == None:
                return None
            if slow_pointer.next == None :
                return None
             
            if slow_pointer.next == fast_pointer.next.next :
                slow_pointer = head
                fast_pointer = fast_pointer.next.next
                while fast_pointer != None :
                    if slow_pointer == fast_pointer :
                        return slow_pointer
                    else :
                        slow_pointer = slow_pointer.next
                        fast_pointer = fast_pointer.next 
            else :
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next 

        return None