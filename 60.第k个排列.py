#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))
        factor = 1
        for i in range(2, n + 1):
            factor *= i
        ans = ""
        while len(nums):
            factor = factor // len(nums)
            ans += str(nums.pop((k - 1) // factor))
            k = (k - 1)  % factor + 1
        return ans
# @lc code=end
