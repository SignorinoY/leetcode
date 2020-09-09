#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target: int, start: int, path: list):
            if target < 0:
                return
            elif target == 0:
                ans.append(path)
                return
            for index, candidate in enumerate(candidates[start:]):
                if target - candidate < 0:
                    break
                dfs(target - candidate, start + index, path + [candidate])
        ans = []
        candidates = sorted(candidates)
        dfs(target, 0, [])
        return ans
# @lc code=end
