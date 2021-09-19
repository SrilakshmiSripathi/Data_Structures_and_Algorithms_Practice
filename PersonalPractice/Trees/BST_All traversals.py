class node:
    """ Tree node constructor, uses linked lists representation"""
    def __init__ (self, value = None):
        self.value = value
        self.left = None
        self.right = None

class BT():
    """ Class BT constructs tree and has 3 traversal methods"""
    def __init__(self):
        """Init constructor to initialize tree"""
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
                if (val <= current.value):
                    current = current.left
                else:
                    current = current.right
            if (val <= root.value):
                root.left = new
            else:
                root.right = new
    def Preorder(self):
        """ Preorder traversal of tree nodes- root, leftchild, rightchild"""
        if self.root != None:
            self.Pre(self.root)

    def Pre(self,currNode):
        """ Recursively helper for preorder traversal"""
        if currNode != None:
            print (currNode.value)
            self.Pre(currNode.left)
            self.Pre(currNode.right)

    def Inorder(self):
        """ Inorder traversal of nodes- leftchild, root, rightchild"""
        if self.root != None:
            self.In(self.root)

    def In(self,currNode):
        """ Inorder method's recursively helper"""
        if currNode != None:
            self.In(currNode.left)
            print (currNode.value)
            self.In(currNode.right)

    def Postorder(self):
        """ Postorder traversal of tree nodes- root, leftchild, rightchild"""
        if self.root != None:
            self.Post(self.root)

    def Post(self,currNode):
        """ Recursively helper for Postorder traversal"""
        if currNode != None:
            self.Post(currNode.left)
            self.Post(currNode.right)
            print (currNode.value)


#Test Function:
def Test():
    some_insta = BT()
    s = [18, 15, 30, 40, 50, 100, 40]
    for _ in s:
        some_insta.insert(_)
    some_insta.Preorder()
    some_insta.Inorder()
    some_insta.Postorder()
Test()
