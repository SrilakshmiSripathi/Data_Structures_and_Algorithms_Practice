from random import randint

# Tree structure
class tree():
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None        
        
# maintain tree structure with addition of numbers
class BST():
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root == None:
            self.root = tree(value)
            #print (self.root,"done")
        else:
            self.inserting(value, self.root)
            
    def inserting(self, value, current_parent):
        if current_parent.left_child == None:
            current_parent.left_child = tree(value)
        elif current_parent.left_child != None:
            return self.inserting(value, current_parent.left_child)

        elif current_parent.right_child == None:
                current_parent.right_child = tree(value)
        elif current_parent.right_child != None:
            return self.inserting(value, current_parent.left_child)

    def show(self):
        if self.root != None:
            self.showing(self.root)

    def showing(self,current):
        if current != None:
            print (str(current.value))
            self.showing(current.left_child)
            self.showing(current.right_child)
            
    def find(self,value):
        if self.root != None:
            return self.findAll(value,self.root)
        else:
            return None
        
    def findAll(self,value,current):
        if value == current.value:
            return current
        elif value < current.value and current.left_child!=None:
            return self.findAll(value, current.left_child)
        elif value > current.value and current.right_child!=None:
            return self.findAll(value, current.right_child)

a = [1,2,3,4,5,6,7,8,9,10,11,12]
b = [1,2,3,4,5,6,7,7,7,7,7,7,7,8,9,11]
instance = BST()
for i in b:
    instance.insert(i)
instance.show()
instance.find(7)
