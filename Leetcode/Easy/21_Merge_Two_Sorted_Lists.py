# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not(list1):
            return list2
        elif not(list2):
            return list1
        
        result = list1 if list1.val < list2.val else list2 # new head node
        if result == list1 :
            list1 = list1.next
        elif result == list2:
            list2 = list2.next

        head = result

        while list1 != None and list2 != None:
            if list1.val <= list2.val :
                result.next = list1 
                list1 = list1.next
            elif list1.val >= list2.val:
                result.next = list2
                list2 = list2.next
            result = result.next

        while list1 != None :
            result.next = list1
            list1 = list1.next
            result = result.next
        while list2 != None:
            result.next = list2 
            list2 = list2.next
            result = result.next
    
        return head