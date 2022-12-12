class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.inorderPointer = None

    def inorder(self):
        global returned
        returned_local = []

        self._inorder(returned_local)

        returned = returned_local
        return returned

    def _inorder(self, returned):
        if self.left_child is not None:
            self.left_child._inorder(returned)
        if len(returned) >= 1:
            returned[len(returned) - 1].inorderPointer = self
        returned.append(self)
        if self.right_child is not None:
            self.right_child._inorder(returned)


returned = []

root = Node("x")

root.left_child = Node("a")
root.right_child = Node("y")

root.left_child.left_child = Node("b")
root.left_child.right_child = Node("c")

root.left_child.left_child.left_child = Node("d")
root.left_child.left_child.right_child = Node("e")

root.left_child.right_child.right_child = Node("f")

root.left_child.left_child.left_child.left_child = Node("g")
root.left_child.left_child.left_child.right_child = Node("h")

root.left_child.left_child.right_child.right_child = Node("i")

root.left_child.right_child.right_child.right_child = Node("k")

root.left_child.left_child.left_child.left_child.left_child = Node("j")
root.left_child.left_child.left_child.left_child.right_child = Node("n")

root.left_child.left_child.left_child.left_child.left_child.left_child = Node("l")

for nodzik in root.inorder():
    print(f"{nodzik, nodzik.inorderPointer} ", end="")
