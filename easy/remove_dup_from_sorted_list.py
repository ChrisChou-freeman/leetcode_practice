from typing import Optional

class ListNode:
    def __init__(self, val: int=0, next: Optional['ListNode']=None):
        self.val = val
        self.next = next

    @classmethod
    def create_new_nodes(cls, ls:list[int]) -> Optional['ListNode']:
        if len(ls) == 0:
            return None
        n_node = cls(ls[0])
        n_next = n_node
        for i in range(1, len(ls)):
            n_next.next = cls(ls[i])
            n_next = n_next.next
        return n_node

    @staticmethod
    def list_all_nodes(nodes: Optional['ListNode']) -> list[int]:
        l: list[int] = []
        while nodes is not None:
            l.append(nodes.val)
            nodes = nodes.next
        return l

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        if start is None:
            return None
        while start.next is not None:
            while start.next is not None and start.val == start.next.val:
                start.next = start.next.next
            start = start.next
            if start is None:
                break
        return head

s = Solution()

result = s.deleteDuplicates(ListNode.create_new_nodes([1, 2, 2]))
print(ListNode.list_all_nodes(result))
result = s.deleteDuplicates(ListNode.create_new_nodes([1, 1, 2, 3, 3]))
print(ListNode.list_all_nodes(result))
result = s.deleteDuplicates(ListNode.create_new_nodes([1, 1, 1]))
print(ListNode.list_all_nodes(result))
