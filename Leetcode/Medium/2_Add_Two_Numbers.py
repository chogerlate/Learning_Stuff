# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # fix length of linked list
        # len_l1 = 
        # len_l2 =
        global carry 
        
        carry  = 0
        answer = ListNode()
        cur_answer = answer
        cur_l1 = l1
        cur_l2 = l2 
        while cur_l1.next != None and cur_l2.next != None :
            
            digit = cur_l1.val + cur_l2.val + carry
            carry = digit//10
            digit = digit % 10

            cur_answer.val = digit  
            
            cur_l1 = cur_l1.next
            cur_l2 = cur_l2.next

            cur_answer.next = ListNode()
            cur_answer = cur_answer.next

        # after we finished loop through some number
        digit = cur_l1.val + cur_l2.val + carry
        carry = digit//10
        digit = digit % 10 
        cur_answer.val = digit
        cur_l1 = cur_l1.next
        cur_l2 = cur_l2.next

        if cur_l1 != None :
            while cur_l1.next != None :
                cur_answer.next = ListNode()
                cur_answer = cur_answer.next

                digit = cur_l1.val + carry
                carry = digit//10
                digit = digit % 10
                cur_answer.val = digit
                cur_l1 = cur_l1.next
            
            cur_answer.next = ListNode()
            cur_answer = cur_answer.next
            digit = cur_l1.val  + carry
            carry = digit//10
            digit = digit % 10
            cur_answer.val = digit
     

        elif cur_l2 != None :
            while cur_l2.next != None :
                cur_answer.next = ListNode()
                cur_answer = cur_answer.next
                digit = cur_l2.val + carry
                carry = digit//10
                digit = digit % 10
                cur_answer.val = digit
                cur_l2 = cur_l2.next

            cur_answer.next = ListNode()
            cur_answer = cur_answer.next
            digit = cur_l2.val  + carry
            carry = digit//10
            digit = digit %10 
            cur_answer.val = digit
            
        if carry != 0 :
            cur_answer.next = ListNode()
            cur_answer = cur_answer.next

            digit = carry
            carry = digit//10
            digit = digit % 10 
            cur_answer.val = digit

        return answer