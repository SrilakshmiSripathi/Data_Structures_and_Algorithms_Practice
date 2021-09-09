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
        if (self.root == None):
            self.root = node(val)
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (val <= current.value):
                    current = current.left
                else:
                    current = current.right
            if (val < parent.value):
                parent.left = node(val)
            else:
                parent.right = node(val)
def LCA(root, n1, n2):
    """ Input: Tree root, node values n1,n2
        Ouput: returns common parent"""
    if root == None:
        return None
    if root == n1 or root == n2:
        return root
    LeftTree = LCA(root.left,n1,n2)
    RightTree = LCA(root.right,n1,n2)

    if LeftTree != None and RightTree != None:
        return root
    elif LeftTree == None and RightTree == None:
        return None
    else:
        return LeftTree if LeftTree is not None else RightTree


some_insta = BT()
s = [18,15,30,40,50,100,40,40]
for _ in s:
    some_insta.insert(_)

print(LCA(some_insta.root,40,15))
  
