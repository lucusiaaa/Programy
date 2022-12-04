class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.globalArr = []

    def preorder(self):
        self.globalArr = [self.value]
        if self.left_child is not None:
            self.globalArr += self.left_child.preorder()
        if self.right_child is not None:
            self.globalArr += self.right_child.preorder()
        return self.globalArr

    def inorder(self):
        self.globalArr = []
        if self.left_child is not None:
            self.globalArr += self.left_child.inorder()
        self.globalArr += self.value
        if self.right_child is not None:
            self.globalArr += self.right_child.inorder()
        return self.globalArr

    def postorder(self):
        self.globalArr = []
        if self.left_child is not None:
            self.globalArr += self.left_child.postorder()
        if self.right_child is not None:
            self.globalArr += self.right_child.postorder()
        self.globalArr += self.value
        return self.globalArr


root = Node("a")

root.left_child = Node("b")
root.right_child = Node("c")

root.left_child.left_child = Node("d")
root.left_child.right_child = Node("e")

print(root.preorder())
print(root.inorder())
print(root.postorder())
