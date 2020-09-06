#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        l_depth = self.minDepth(root.left)
        r_depth = self.minDepth(root.right)
        if root.left and root.right:
            return min(l_depth, r_depth) + 1
        else:
            return l_depth + r_depth + 1
# @lc code=end
