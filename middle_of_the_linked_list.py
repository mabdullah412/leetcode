# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # traverse 1
        length = 0
        temp = head
        while temp != None:
            temp = temp.next
            length += 1

        # calculate mid
        mid = int(length / 2) + 1
        print(length, mid)

        if length == 1:
            return head

        # traverse 2
        length = 0
        temp = head

        while temp != None:
            temp = temp.next
            length += 1

            if length + 1 == mid:
                break

        return temp
        