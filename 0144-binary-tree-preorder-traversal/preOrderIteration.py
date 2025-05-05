class Solution:
    def preOrder(self, root):
        nums = []
        if root is None:
            return nums
        st = []
        st.append(root)

        while st:
            root = st.pop()
            nums.append(root.val)

            if root.right:
                st.append(root.right)
            
            if root.left:
                st.append(root.left)
        return nums