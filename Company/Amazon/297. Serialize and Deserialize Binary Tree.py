"""
This is a very wise method. We use the pre-order tree iteration.
In this method, a very important characteristic of Python is included. Iteration.
a = iter(list): return a iteration structure.
b = next(a): return each item in a.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize1(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def DFS(res, node):
            if node:
                res.append(str(node.val))
                DFS(res, node.left)
                DFS(res, node.right)
            else:
                res.append('#')
        res = []
        DFS(res, root)
        return ' '.join(res)

    def deserialize1(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def DFS():
            pointer = next(data_list)
            if pointer != '#':
                node = TreeNode(pointer)
                node.left = DFS()
                node.right = DFS()
                return node
            else:
                return None
        data_list = iter(data.split())
        return DFS()

    def serialize2(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        return root.val, self.serialize2(root.left), self.serialize2(root.right)

    def deserialize2(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data[0] == '#':
            return None
        node = TreeNode(data[0])
        node.left = self.deserialize2(data[1])
        node.right = self.deserialize2(data[2])
        return node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

