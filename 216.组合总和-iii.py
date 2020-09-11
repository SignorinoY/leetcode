#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(target: int, start: int, path: list):
            if target < 0 or len(path) > k:
                return
            elif target == 0 and len(path) == k:
                ans.append(path)
                return
            for index, candidate in enumerate(candidates[start:]):
                if target - candidate < 0:
                    break
                dfs(target - candidate, start + index + 1, path + [candidate])
        ans = []
        candidates = range(1, 10)
        dfs(n, 0, [])
        return ans
# @lc code=end
