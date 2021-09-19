class node:
    def __init__(self, root = None):
        self.root = root
        self.left = None
        self.right = None

    def Range2(self, node, k1, k2, count):
        if node == None:
            return count
        else:
            if k1 <= node  and node <= k2:
                print node
                count += 1
            self.Range2(node.left, k1, k2, count)
            self.Range2(node.right, k1, k2, count)
            if self.root < k1:
                self.Range2(node.right, k1, k2, count)
            elif self.root > k2:
                self.Range2(node.left, k1, k2, count)

def test():
    insta = node()
    insta.root =  18
    insta.left = 12
    insta.right =  20
    insta.left.left = 10
    insta.right.left = 13
    print insta.Range2(insta.root, 15, 22, 0)
test()
    
