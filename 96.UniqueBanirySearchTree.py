# 96.UniqueBanirySearchTree
# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
class Solution:
    def numTrees(self, n: int) -> int:
        uniq_tree = [1] * (n + 1)
        
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                total += uniq_tree[root - 1] * uniq_tree[nodes - root]
            uniq_tree[nodes] = total
        
        return uniq_tree[n]
# Example usage
if __name__ == "__main__":
    sol = Solution()
    n = 3
    result = sol.numTrees(n)
    print(f"Number of unique BSTs for n={n}: {result}")