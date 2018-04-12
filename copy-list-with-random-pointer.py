"""
https://leetcode.com/submissions/detail/149677650/


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

        pointer = head
        backup = {}
        while pointer:
            point_id = id(pointer)
            backup[point_id] = {'label': pointer.label,
                                'next_id': id(pointer.next) if pointer.next else 0,
                                'random': id(pointer.random) if pointer.random else 0,
                                'new_node': RandomListNode(pointer.label)}
            pointer = pointer.next

        for obj_id, info_dict in backup.items():
            next_id = info_dict['next_id']
            info_dict['new_node'].next = backup[next_id]['new_node'] if next_id != 0 else None

            random_id = info_dict['random']
            info_dict['new_node'].random = backup[random_id]['new_node'] if random_id != 0 else None
        return backup[id(head)]['new_node']

            