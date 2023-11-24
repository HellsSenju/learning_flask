class TreeNode:
    def __init__(self, val=0, entropy=0, left=None, right=None):
        self.val = val
        self.entropy = entropy
        self.left = left
        self.right = right

    def from_list(l):
        nodes = [TreeNode(v) for v in l]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root


t = TreeNode.from_list([4, 2, 7, 1, 3, 6, 9])
print(t)
