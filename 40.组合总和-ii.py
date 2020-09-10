#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target: int, start: int, path: list):
            if target < 0:
                return
            elif target == 0 and path not in ans:
                ans.append(path)
                return
            for index, candidate in enumerate(candidates[start:]):
                if target - candidate < 0:
                    break
                dfs(target - candidate, start + index + 1, path + [candidate])
        ans = []
        candidates = sorted(candidates)
        dfs(target, 0, [])
        return ans
# @lc code=end
