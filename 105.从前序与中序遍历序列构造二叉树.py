#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def _buidTree(prestart: int, instart: int, count: int):
            if count == 0:
                return None
            idx = inorder_idx[preorder[prestart]] - instart
            root = TreeNode(preorder[prestart])
            root.left = _buidTree(prestart+1, instart, idx)
            root.right = _buidTree(prestart+idx+1, instart+idx+1, count-idx-1)
            return root
        inorder_idx = {elem: i for i, elem in enumerate(inorder)}
        return _buidTree(0, 0, len(preorder))
# @lc code=end
