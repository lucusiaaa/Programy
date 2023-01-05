class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f"{self.left_child.value if self.left_child is not None else ''} {self.value} {self.right_child.value if self.right_child is not None else ''}"

    # This function sorts the parent and child values so that the largest value is in the right child
    # and the smallest value is in the left child
    def sortInNode(self):
        if self.left_child is not None and self.value <= self.left_child.value:
            self.value, self.left_child.value = self.left_child.value, self.value
        if self.right_child is not None and self.value > self.right_child.value:
            self.value, self.right_child.value = self.right_child.value, self.value
        if self.left_child is not None and self.value <= self.left_child.value:
            self.value, self.left_child.value = self.left_child.value, self.value

    # This function is a postorder traversal of tree.
    def postorder(self):
        if self.left_child is not None:
            self.left_child.postorder()
        if self.right_child is not None:
            self.right_child.postorder()
        self.sortInNode()


root = Node(3)

root.left_child = Node(15)
root.right_child = Node(8)

root.left_child.left_child = Node(7)
root.left_child.right_child = Node(1)
root.right_child.left_child = Node(0)

root.left_child.left_child.left_child = Node(23)

root.left_child.right_child.right_child = Node(6)
root.left_child.right_child.right_child.left_child = Node(10)

root.left_child.left_child.left_child.right_child = Node(26)
root.left_child.left_child.left_child.right_child.right_child = Node(5)

root.postorder()

print(root)
