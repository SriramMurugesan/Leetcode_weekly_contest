class Solution:
    def maxScore(self, parent: list[int], op: list[int], score: list[int]) -> int:
        if not parent:
            return 0
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1,n):
            # adding children nodes for corresponding parent node 
            children[parent[i]].append(i)
        # print(children)
        def dfs(u):
            if not children[u]:
                return score[u]
            # find scores of child 
            child_scores = [dfs(v) for v in children[u]]
            total_sum = sum(child_scores) + score[u]
            min_score=min(child_scores)
            # print(u,child_scores,total_sum,min_score)

            if op[u]==1:
                return total_sum-min_score
            else:
                return total_sum-min(min_score,0) 
        return dfs(0)
            
        