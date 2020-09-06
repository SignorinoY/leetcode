#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
        return [frequencies[i][0] for i in range(k)]
# @lc code=end
