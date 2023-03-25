# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head # define the traveller 
        len_list = 0 # define the varible that will be used to store our length of the list

        # Base case
        if not head : 
            return head
        
        # count the length of the list
        while cur != None :
            cur = cur.next
            len_list += 1
        
        # calculate the middle of the list
        middle = len_list//2 + 1
        
        cur_index = 1 # current index pointer
        answer = head # define a variable to hold the answer
        
        # loop until we reach the middle of the list
        while cur_index < middle :
              answer = answer.next  
              cur_index += 1 

        return answer