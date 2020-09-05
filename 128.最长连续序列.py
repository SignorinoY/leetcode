#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        hash_set = set(nums)
        for num in hash_set:
            if num - 1 not in hash_set:
                cur_num = num
                cur_len = 1
                while cur_num + 1 in hash_set:
                    cur_num += 1
                    cur_len += 1
                max_len = max(max_len, cur_len)
        return max_len
# @lc code=end

