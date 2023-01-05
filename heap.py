class Heap:
    def __init__(self):
        self.heap_arr = []

    def __str__(self):
        return str(self.heap_arr)

    # This function returns True if the heap is empty and False if is not.
    def isEmpty(self):
        return len(self.heap_arr) == 0

    # This function changes k-th node in a Heap with parent node if parent node is grater than k-th node.
    def bubbleSortBottomToUp(self, idx):
        parent_idx = int((idx - 1) / 2)
        if self.heap_arr[idx] < self.heap_arr[parent_idx]:
            self.heap_arr[idx], self.heap_arr[parent_idx] = self.heap_arr[parent_idx], self.heap_arr[idx]
            self.bubbleSortBottomToUp(parent_idx)

    # This function changes parent node in a Heap with children which has got lower value than the parent node.
    def bubbleSortUpToBottom(self, idx):
        low = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        changed = False

        if left < len(self.heap_arr) and self.heap_arr[left] < self.heap_arr[low]:
            low = left
            changed = True
        if right < len(self.heap_arr) and self.heap_arr[right] < self.heap_arr[low]:
            low = right
            changed = True
        if changed:
            self.heap_arr[idx], self.heap_arr[low] = self.heap_arr[low], self.heap_arr[idx]
            self.bubbleSortUpToBottom(low)

    # This function adds element to the Heap and push this element to proper place in the Heap
    # by using bubbleSortBottomToUp() function
    def add(self, elem):
        self.heap_arr.append(elem)
        self.bubbleSortBottomToUp(len(self.heap_arr) - 1)

    # This function removes the smallest element (root) from Heap and sorts all elements
    # by using bubbleSortUpToBottom() function so that the smallest element that remains in the heap becomes the root
    def removeMin(self):
        last = self.heap_arr.pop(-1)
        self.heap_arr[0] = last
        self.bubbleSortUpToBottom(0)


inputs = [30, 15, 3, 5, 60, 0, 12, 4, 6, 7, 21, 13, 25, 27, 39, 47, 56, 23, 45, 76, 345, 57, 44]

heap = Heap()
for input in inputs:
    heap.add(input)

heap.removeMin()

print(heap)
