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
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode()
        prev = head
        while any(item for item in lists):
            vals = [item.val if item else 1e5 for item in lists]
            val_min = min(vals)
            idx = vals.index(val_min)
            prev.next = lists[idx]
            prev = prev.next
            lists[idx] = lists[idx].next
        return head.next

# @lc code=end
