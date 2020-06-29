class Node:
    
    def __init__(self, val= None):
        self.root = val
        self.left = None
        self.right = None
        
    def sortedArrayToBST(self, ar):
        if len(ar) == 0:
            return None
        else:
            mid = (len(ar))//2
            root = Node(mid)
            root.left = self.sortedArrayToBST(ar[:mid-1])
            root.right = self.sortedArrayToBST(ar[mid+1:])
        return self.out(root)
    
    def out(self,c_node):
        if c_node != None:
            print c_node
            self.out(c_node.left)
            self.out(c_node.right)

array = [1,2,3,4,5,6,7,8,9,10,11,12]
insta = Node()
print insta.sortedArrayToBST(array)

