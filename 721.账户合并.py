#
# @lc app=leetcode.cn id=721 lang=python3
#
# [721] 账户合并
#

# @lc code=start
import collections

class UnionFind:

    def __init__(self) -> None:
        self.parent = {}
        self.size = {}

    def find(self, x: any) -> int:
        self.parent.setdefault(x, x)
        while x != self.parent[x]:
            x = self.parent[x]
        return x
    
    def union(self, p: any, q: any) -> None:
        p_root, q_root = self.find(p), self.find(q)
        if p_root == q_root:
            return
        self.size.setdefault(p_root, 1)
        self.size.setdefault(q_root, 1)
        if self.size[p_root] < self.size[q_root]:
            self.parent[p_root] = q_root
            self.size[q_root] += self.size[p_root]
            del self.size[p_root]
        else:
            self.parent[q_root] = p_root
            self.size[p_root] += self.size[q_root]
            del self.size[q_root]

class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        name_dict = {}
        uf = UnionFind()
        for account in accounts:
            for email in account[1:]:
                if email not in name_dict:
                    name_dict[email] = account[0]
                uf.union(account[1], email)
        res = collections.defaultdict(list)
        for email in name_dict:
            res[uf.find(email)].append(email)
        return [[name_dict[key]] + sorted(value) for key, value in res.items()]

# @lc code=end
