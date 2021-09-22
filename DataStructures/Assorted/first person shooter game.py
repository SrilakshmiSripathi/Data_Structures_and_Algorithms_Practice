# locate shooters
# divide players in to zones so that its divided equally
## Solution
## 1. Convert players(x,y) to polar co-ordinates (R,thetha);
## 2. sort the players according to thetha
## 3. Perform BST using thetha value on the sorted list
## 4. Add pi to theta to get partitions

import math
class Node():
    """Tree node constructor"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BST():
    def __init__(self):
        self.root = None

    def insert (self, val):
        """ Method to insert a value to the tree, at right spot"""
        new = Node(val)
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

    def Print(self):
        ## Print tree nodes inorder to get sorted theta values
        inorder = None
        if self.root != None:
            inorder = self.InIter(self.root)
        return inorder

    def InIter(self, CurrNode):
        ## iterative inorder
        visited, stack = [], []
        while stack or CurrNode:
            if CurrNode:
                stack.append(CurrNode)
                CurrNode = CurrNode.left
            else:
                tmpNode = stack.pop()
                visited.append(tmpNode.value)
                CurrNode = tmpNode.right
        return visited
    
def Polar(tup):
    ## Function to generate polar co-ordinates
    di = {}
    for i in tup:
        x = i[0]
        y = i[1]
        r = math.sqrt(x**2 + y**2)
        thetha = math.atan2(y,x)
        di.update({thetha:r})
    print ("theta and radius= ",di)
    return di

def GenTree(cartesianCo):
    ## Construct BST function using polar co-ordinates
    PolarCo = Polar(cartesianCo)
    T = BST()
    for co in PolarCo:
        T.insert(co)
    SortedTheta = T.Print()
    return Zone(SortedTheta)

# Divides players in roughly equal size and returns no of zones
def Zone(thetas):
    '''Input: sorted Theta values
    Output: Number of partitions'''
    partition = {}
    for angle in thetas:
        Zones = int(angle + math.pi)
        partition[Zones] = partition.get(Zones, 0) + 1
    return "Number of partitions=", len(partition)
    
PlayersCo = [(1,5),(-1,5),(4,3),(-4,4),(-1,-7),(1,-5),(2,4),(-4,-3),(2,-4)]
print (GenTree(PlayersCo))
players = [(1,7),(-6,5),(2,-3),(-4,-1),(6,-2),(-1,-3),(-4,-5),(-3,7),]
print (GenTree(players))
