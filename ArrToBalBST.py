class Node:
    __slots__ = 'value','left','right'

    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value == data:
            return "Tree already contains data: " + str(data)
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)

    def search(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.value))
            if self.right:
                self.right.inorder()

class Tree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)

    def search(self, data):
        if self.root:
            return self.root.search(data)
        else:
            return "Cannot find data: " + str(data)

    def setRootVal(self, val):
        self.root.value = val

    def getLeftChild(self):
        return self.root.left

    def getRightChild(self):
        return self.root.right

    def preorder(self):
        print("PreOrder")
        self.root.preorder()

    def postorder(self):
        print("PostOrder")
        self.root.postorder()

    def inorder(self):
        print("InOrder")
        self.root.inorder()

    def height(self, node):
        if self.root is None:
            return 0
        else:
            return max(self.height(node.leftChild), self.height(node.rightChild)) + 1


def __ArrToBalBST(array, start, end):
    if start > end:
        return None
    mid = int(start + (end - start) / 2) # Avoid integer overflow
    node = Node(array[mid])
    node.left = __ArrToBalBST(array, start, mid-1)
    node.right = __ArrToBalBST(array, mid+1, end)
    return node

def ArrToBalBST(array, n):
    tree = Tree()
    tree.root = __ArrToBalBST(array, 0, n-1)
    return tree

array = [0,1,2,3,4,5,6,7,8,9]
n = len(array)
tree = ArrToBalBST(array, n)
tree.inorder()