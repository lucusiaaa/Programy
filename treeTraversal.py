class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def preorder(self):
        returned = [self.value]
        if self.left_child is not None:
            returned += self.left_child.preorder()
        if self.right_child is not None:
            returned += self.right_child.preorder()
        return returned

    def inorder(self):
        returned = []
        if self.left_child is not None:
            returned += self.left_child.inorder()
        returned.append(self.value)
        if self.right_child is not None:
            returned += self.right_child.inorder()
        return returned

    def postorder(self):
        returned = []
        if self.left_child is not None:
            returned += self.left_child.postorder()
        if self.right_child is not None:
            returned += self.right_child.postorder()
        returned.append(self.value)
        return returned


root = Node("a")

root.left_child = Node("b")
root.right_child = Node("c")

root.left_child.left_child = Node("d")
root.left_child.right_child = Node("e")

print(root.preorder())
print(root.inorder())
print(root.postorder())
