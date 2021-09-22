import binarysearch

class node:
    def __init__(self, root):
        self.root = None
        self.left = None
        self.right = None

    def Range2(self, node, k1, k2, count = None):
        if self.node == None:
            return count
        else:
            if k1 <= self.node <= k2:
                count += 1
            self.Range2(node.left,k1,k2, count)
            self.Range2(node.left,k1,k2, count)
