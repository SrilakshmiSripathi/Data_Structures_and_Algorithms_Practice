import random

# Tree structure
class tree():
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None        
        
# maintain tree structure with addition of numbers
class BT():
    def __init__(self):
        self.root = None
        
    def Insert(self,value):
        if self.root == None:
            self.root = tree(value)
        else:
            self.insertion(value, self.root)
            
    def insertion(self, value, cp):
        if value < cp.value:
            if cp.left == None:
                cp.left = tree(value)
            else:
                self.insertion(value, cp.left)
        elif value > cp.value:
            if cp.right == None:
                cp.right = tree(value)
            else:
                self.insertion(value, cp.right)
                
    def pr(self):
        if self.root != None:
            self._pr(self.root)

    def _pr(self,current):
        if current != None:
            self._pr(current.left)
            print str(current.value)
            self._pr(current.right)

c = BT()
for i in range(10):
    c.Insert(i)
print c

