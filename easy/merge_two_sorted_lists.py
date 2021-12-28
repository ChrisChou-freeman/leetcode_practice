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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list: Optional[ListNode] = None
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            merged_list = list2
        elif list2 is None:
            merged_list = list1
        else:
            merged_list = list1
            next_node = merged_list
            while next_node.next is not None:
                next_node = next_node.next
            next_node.next = list2
        node1 = merged_list
        while node1 is not None:
            node2 = node1.next
            while node2 is not None:
                if node1.val > node2.val:
                    n1 = node1.val
                    node1.val = node2.val
                    node2.val = n1
                node2 = node2.next
            node1 = node1.next
        return merged_list

list1 = ListNode.create_new_nodes([1, 2, 4])
list2 = ListNode.create_new_nodes([1, 3, 4])

s = Solution()
n_list = s.mergeTwoLists(list1, list2)

assert ListNode.list_all_nodes(n_list) == [1, 1, 2, 3, 4, 4]

n_list = s.mergeTwoLists(None, ListNode(1))
assert ListNode.list_all_nodes(n_list) == [1]

n_list = s.mergeTwoLists(ListNode(1), None)
assert ListNode.list_all_nodes(n_list) == [1]
