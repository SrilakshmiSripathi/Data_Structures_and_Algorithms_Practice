import random

# Tree structure
class Tree():
    def __init__(self,root=None):
        self.root = root
        self.left = None
        self.right = None        
        
# maintain tree structure with addition of numbers
class BST():
    def __init__(self):
        self.root = None
        
    def insert(self,node):
        if self.root == None:
            self.root = Tree(node)
        else:
            self._insert(node,self.root)
            
    def _insert(self,value,current_node):
        if value < current_node:
            if current_node.left == None:
                current_node.left = Tree(value)
            else:
                self._insert(value,current_node.left)
        elif value > current_node:
            if current_node.right == None:
                current_node.right = Tree(value)
            else:
                self._insert(value,current_node.left)
    def pr(self, node):
        if node != None:
            print (node)
            return pr(self,node.right), pr(self,node.left)

    def Range2(self, node, k1, k2, count = None):
        if node == None:
            return count
        else:
            if k1 <= node  and node <= k2:
                print (node)
                count += 1
            self.Range2(node.left, k1, k2, count)
            self.Range2(node.right, k1, k2, count)
            if self.root < k1:
                self.Range2(node.right, k1, k2, count)
            elif self.root > k2:
                self.Range2(node.left, k1, k2, count)

def test():
    insta = BST()
    for i in range(20):
        insta.insert(i)
    print (insta.Range2(insta.root, 2,10))
test()
    
    


