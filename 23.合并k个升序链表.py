#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappop, heappush


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for node in lists:
            while node:
                heappush(heap, node.val)
                node = node.next
        head = ListNode()
        prev = head
        while heap:
            prev.next = ListNode(heappop(heap))
            prev = prev.next
        return head.next

# @lc code=end
