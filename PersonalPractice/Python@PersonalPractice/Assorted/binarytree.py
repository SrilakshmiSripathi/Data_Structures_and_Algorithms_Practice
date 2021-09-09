class node():
    """Tree node constructor, uses likedlists representation"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BT():
    """class BT constructs tree and has 3 traversal methods"""
    def __init__(self):
        
        self.root = None
        
    def insert (self, val):
        """ Method to insert a value to the tree, at right spot"""
        new = node(val)
        if (self.root == None):
            self.root = new
        else:
            current = self.root
            while (current != None):
                root = current
                if (val < current.value):
                    current = current.left
                else:
                    current = current.right
            if (val < root.value):
                root.left = new
            else:
                root.right = new
            
    def Preorder(self):
        """ Preorder traversal of tree nodes- root,leftchild,rightchild"""
        if self.root != None:
            self.Pre(self.root)

    def Pre(self,currNode):
        """ Recursively helper for preorder traversal"""
        if currNode != None:
            print (currNode.value)
            self.Pre(currNode.left)
            self.Pre(currNode.right)

    def Inorder(self):
        """ Preorder traversal of tree nodes- root,leftchild,rightchild"""
        if self.root != None:
            self.In(self.root)

    def In(self,currNode):
        """ Recursively helper for preorder traversal"""
        if currNode != None:
            self.In(currNode.left)
            print (currNode.value)
            self.In(currNode.right)

some_insta = BT()
s = [12, 35, 50, 15, 31, 22, 25, 44, 66, 24, 90, 70, 4, 10, 18]

'''
               25
        15            50
    10     22     35      70
   4 12   18 24  31 44   66 90
'''
#s = [1,2,3,4,5]
for _ in s:
    some_insta.insert(_)
some_insta.Preorder()
print()
some_insta.Inorder()

