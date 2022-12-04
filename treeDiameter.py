class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    # Returns array of integers with left and right deeps of node and integer representation
    # max diameter of tree on which the function is called.
    def deepness(self):
        maxDiameter = 0
        diameter = 0
        if self.left_child is not None:
            result, diameter = self.left_child.deepness()
            left_deep = 1 + max(result[0], result[1])
        else:
            left_deep = 0
        if diameter > maxDiameter:
            maxDiameter = diameter

        if self.right_child is not None:
            result, diameter = self.right_child.deepness()
            right_deep = 1 + max(result[0], result[1])
        else:
            right_deep = 0

        if diameter > maxDiameter:
            maxDiameter = diameter

        if left_deep + right_deep > maxDiameter:
            maxDiameter = left_deep + right_deep

        return [left_deep, right_deep], maxDiameter


# root = Node("x")
#
# root.left_child = Node("a")
# root.right_child = Node("y")
#
# root.left_child.left_child = Node("b")
# root.left_child.right_child = Node("c")
#
# root.left_child.left_child.left_child = Node("d")
# root.left_child.left_child.right_child = Node("e")
#
# root.left_child.right_child.right_child = Node("f")
#
# root.left_child.left_child.left_child.left_child = Node("g")
# root.left_child.left_child.left_child.right_child = Node("h")
#
# root.left_child.left_child.right_child.right_child = Node("i")
#
# root.left_child.right_child.right_child.right_child = Node("k")
#
# root.left_child.left_child.left_child.left_child.left_child = Node("j")
# root.left_child.left_child.left_child.left_child.right_child = Node("n")
#
# root.left_child.left_child.left_child.left_child.left_child.left_child = Node("l")


root = Node("F")

root.left_child = Node("E")
root.right_child = Node("K")

root.left_child.left_child = Node("R")
root.left_child.right_child = Node("D")

root.right_child.left_child = Node("O")
root.right_child.right_child = Node("T")

root.left_child.left_child.left_child = Node("P")

root.left_child.left_child.left_child.right_child = Node("I")

root.right_child.left_child.left_child = Node("J")
root.right_child.left_child.left_child.right_child = Node("A")
root.right_child.left_child.left_child.right_child.right_child = Node("C")
root.right_child.left_child.left_child.right_child.right_child.right_child = Node("Z")
root.right_child.left_child.left_child.right_child.right_child.right_child.right_child = Node("Y")
root.right_child.left_child.left_child.right_child.right_child.right_child.right_child.right_child = Node("N")
root.right_child.left_child.left_child.right_child.right_child.right_child.right_child.right_child.right_child = Node("B")


print(root.deepness()[1])
