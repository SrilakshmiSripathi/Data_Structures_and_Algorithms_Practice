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
        
    def find(self, k):
        current = self.root
        s = 0
        while ((current != None) and (current.value != k)):
            if k < current.value:
                current = current.left
            elif k > current.value:
                current = current.right
            elif current.value == k:
                s = s + 1
        return s

some_insta = BT()
s = [18,15,30,40,50,100,40,40]
for _ in s:
    some_insta.insert(_)
some_insta.find(40)
