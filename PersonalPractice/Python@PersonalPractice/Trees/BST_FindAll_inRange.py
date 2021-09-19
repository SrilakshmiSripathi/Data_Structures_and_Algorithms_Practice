import binarytree

def find(tree, k):
    current = tree.root
    s = 0
    while ((current != None) and (current.value != k)):
        if k < current.value:
            current = current.left
        elif k > current.value:
            current = current.right
        elif current.value == k:
            s = s + 1
    return s

insta = binarytree.BT()
print find(insta,40)

