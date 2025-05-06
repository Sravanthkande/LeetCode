class Solution:
    def traversal(self, root):
        Pre, In, Post = [], [], []

        if root is None:
            return [In, Pre, Post]
        
        stack = [(root, 1)]

        while stack:
            node, state = stack.pop()

            if state == 1:
                Pre.append(node.data)
                stack.append((node, 2))

                if node.left:
                    stack.append((node.left, 1))
            elif state == 2:
                In.append(node.data)
                stack.append((node, 3))

                if node.right:
                    stack.append((node.right, 1))
            else:
                Post.append(node.data)
        return [In, Pre, Post]
