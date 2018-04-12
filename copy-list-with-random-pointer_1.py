"""
https://leetcode.com/submissions/detail/149675089/


A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.



Return a deep copy of the list.
"""


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None

        origin = head
        backup = {}
        new_node = {}
        while head:
            head_id = id(head)
            backup[head_id] = {'label': head.label, 'next_id': id(head.next) if head.next else 0, 'random': id(head.random) if head.random else 0}
            new_node[head_id] = RandomListNode(head.label)
            head = head.next

        for obj_id, node in new_node.items():
            next_id = backup[obj_id]['next_id']
            node.next = new_node[next_id] if next_id != 0 else None
            
            random_id = backup[obj_id]['random']
            node.random = new_node[random_id] if random_id != 0 else None
        return new_node[id(origin)]
            
            