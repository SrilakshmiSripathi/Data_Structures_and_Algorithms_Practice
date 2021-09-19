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
                
    def Inorder(self):
        """ Inorder traversal of nodes- leftchild,root,rightchild"""
        if self.root != None:
            self.In(self.root)

    def In(self,currNode):
        """ Inorder method's recursively helper"""
        if currNode != None:
            self.In(currNode.left)
            print currNode.value
            self.In(currNode.right)
            
    def Preorder(self):
        """ Preorder traversal of tree nodes- root,leftchild,rightchild"""
        if self.root != None:
            self.Pre(self.root)

    def Pre(self,currNode):
        """ Recursively helper for preorder traversal"""
        if currNode != None:
            print currNode.value
            self.Pre(currNode.left)
            self.Pre(currNode.right)
            
    def Postorder(self):
        """ Postorder traversal of tree nodes- root,leftchild,rightchild"""
        if self.root != None:
            self.Post(self.root)

    def Post(self,currNode):
        """ Recursively helper for Postorder traversal"""
        if currNode != None:
            self.Post(currNode.left)
            self.Post(currNode.right)
            print currNode.value

    def Ra(self, k1, k2):
        if self.root != None:
            count = 0
            return self.Range2(self.root, k1, k2, count)
        
    def Range2(self, node, k1, k2, c):
        if node == None:
            return c
        else:
            if k1 <= node and node <= k2:
                c += 1
                self.Range2(node.left, k1, k2, c)
                self.Range2(node.right, k1, k2, c)
                return c 
            elif node < k1:
                return self.Range2(node.right, k1, k2, c)
            elif node > k2:
                return self.Range2(node.left, k1, k2, c)


array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
ins = BT()
for x in array:
    ins.insert(x)
ins.Preorder()
ins.Ra(10,15)


##
##some_insta = BT()
##s = [18,15,30,40,50,100,40]
##for _ in s:
##    some_insta.insert(_)
##some_insta.Preorder()
##print some_insta.Ra(10,52)
##
##print "\n"
##some_insta.Inorder()
##print "\n"
##some_insta.Postorder()
##
##print "\n \n \n"
##some = BT()
##k = [1,2,3,4,5]
##for _ in k:
##    some.insert(_)
##some.Preorder()
##print "\n \n \n"
##some.Inorder()
##print "\n \n \n"
##some.Postorder()
##print "\n \n \n"
##
##insta = BT()
##p=[4,1,3,2,7,5]
##for _ in p:
##    insta.insert(_)
##insta.Preorder()
##print "\n \n \n"
##insta.Inorder()
##print "\n \n \n"
##insta.Postorder()
##print "\n \n \n"
