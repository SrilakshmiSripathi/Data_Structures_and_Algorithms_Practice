 def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Use Depth first Search
        def dfs(root,res):
            l,r = 0,0
            # Recursively check left and right subtrees
            if root.left:
                l = dfs(root.left,res)
                if root.left.val == root.val:
                    l += 1
                else:
                    l = 0
            if root.right:
                r = dfs(root.right,res)
                if root.right.val == root.val:
                    l += 1
                else:
                    l = 0
            # Consider the max of 
            res[0] = max(res[0], r + l)
            return max(l, r)
               

        if not root:
            return 0
        res = [0]
        dfs(root, res)
        return res[0]


# or

def longestUnivaluePath(self, root):
        # Final path
        self.ans = 0

        def arrow_length(node):
            # if node is null return, base case for recursion
            if not node:
                return 0
            # Recursively check left and right subtrees
            left_tree = arrow_length(node.left)
            right_tree = arrow_length(node.right)
            
            left_arrow = right_arrow = 0
            # if left node is not null and,
            # isequal to current root then extend path
            if node.left and node.left.val == node.val:
                left_arrow = left_tree + 1
            # if right node is not null and,
            # isequal to current root then extend path
            if node.right and node.right.val == node.val:
                right_arrow = right_tree + 1
            self.ans = max(self.ans, left_arrow + right_arrow)

            # Final maximum path
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans
