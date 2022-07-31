class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def dfs(v, p, q):
    if not v:
        return None, 0
    elif v.val == p or v.val == q:
        return (v, 2) if dfs(v.left, p, q)[1] == 1 or dfs(v.right, p, q)[1] == 1 else (None, 1)
    else:
        left, l_count = dfs(v.left, p, q)
        if left:
            return left, l_count
        right, r_count = dfs(v.right, p, q)
        if right:
            return right, r_count
        return (v, 2) if l_count == 1 and r_count == 1 else (None, max(l_count, r_count))


def lowestCommonAncestor(root, p, q):
    return dfs(root, p.val, q.val)[0].val
