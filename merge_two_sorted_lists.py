"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order."""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0) # Create a dummy node to be the anchor
        tail = dummy # The pointer of the result list

        while list1 and list2: # If both list1 and list2 exist
            if list1.val <= list2.val: # The current value in list1 smaller than the current value in list2
                tail.next = list1 # Add the current node in list1 to the result list
                list1 = list1.next # Move the pointer of list1 to the next node
            else:
                tail.next = list2 # Add the current node in list2 to the result list
                list2 = list2.next # Move the pointer of list2 to the next node
            tail = tail.next # Move the point of the result list to the next node

        if list1: # If only list 1 exist
            tail.next = list1 # Add list1 to the result list
        elif list2:
            tail.next = list2 # Add list2 to the result list

        return dummy.next # Return the result list