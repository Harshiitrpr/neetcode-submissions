"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        if not head:
            return head
        while curr:
            tmp = curr.next
            curr.next = Node(curr.val)
            curr.next.next = tmp
            curr = tmp
        curr = head
        while curr:
            copy = curr.next
            if curr.random:
                copy.random = curr.random.next
            curr = copy.next
        ans = head.next
        curr1, curr2 = head, ans
        while curr1 and curr2:
            curr1.next = curr2.next
            if curr2.next:
                curr2.next = curr2.next.next
            curr1 = curr1.next
            curr2 = curr2.next
            
        return ans