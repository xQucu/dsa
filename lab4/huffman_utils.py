class MinHeap():
    def __init__(self):
        self.data: list[tuple[int, any]] = [0] * 10000
        self.length = 0

    def insert(self, value):
        self.data[self.length] = value
        self._heapifyUp(self.length)
        self.length += 1

    # def len()

    def delete(self):
        if self.length == 0:
            raise IndexError("Can't delete from empty heap")
            # return None
        out = self.data[0]
        self.length -= 1

        if self.length == 0:
            return out

        self.data[0] = self.data[self.length]
        self._heapifyDown(0)
        return out

    def _heapifyDown(self, idx: int) -> None:
        if idx == self.length:
            return

        currVal = self.data[idx]

        idxOfSmallestPriority = idx
        rightIdx = self._rightChild(idx)
        leftIdx = self._leftChild(idx)

        if leftIdx < self.length and self.data[leftIdx][0] < self.data[idxOfSmallestPriority][0]:
            idxOfSmallestPriority = leftIdx

        if rightIdx < self.length and self.data[rightIdx][0] < self.data[idxOfSmallestPriority][0]:
            idxOfSmallestPriority = rightIdx

        if idxOfSmallestPriority == idx:
            return

        self.data[idx] = self.data[idxOfSmallestPriority]
        self.data[idxOfSmallestPriority] = currVal
        self._heapifyDown(idxOfSmallestPriority)

    def _heapifyUp(self, idx: int) -> None:
        if idx == 0:
            return
        pIdx = self._parent(idx)
        pVal = self.data[pIdx]
        pPriority = pVal[0]
        currVal = self.data[idx]
        currPriority = currVal[0]
        if pPriority > currPriority:
            self.data[pIdx] = currVal
            self.data[idx] = pVal
            self._heapifyUp(pIdx)

    def _parent(self, idx: int) -> int:
        return (idx-1)//2

    def _leftChild(self, idx: int) -> int:
        return (idx * 2 + 1)

    def _rightChild(self, idx: int) -> int:
        return (idx * 2 + 2)


class Node():
    def __init__(self, priority, val):
        self.priority = priority
        self.val = val
        self.left = None
        self.right = None


def build_codes(node, prefix, codebook):
    if node is None:
        return
    if node.val is not None:
        codebook[node.val] = prefix
        return
    build_codes(node.left, prefix + "0", codebook)
    build_codes(node.right, prefix + "1", codebook)


def huffman_coding(text: str):
    occurrences = {}
    for c in text:
        if c in occurrences:
            occurrences[c] += 1
        else:
            occurrences[c] = 1

    heap = MinHeap()

    for char, freq in occurrences.items():
        heap.insert((freq, Node(freq, char)))

    while heap.length > 1:
        freq1, leftNode = heap.delete()
        freq2, rightNode = heap.delete()
        merged = Node(freq1 + freq2, None)
        merged.left = leftNode
        merged.right = rightNode
        heap.insert((merged.priority, merged))

    root = heap.delete()[1]
    codebook = {}
    build_codes(root, "", codebook)

    encoded = "".join(codebook[c] for c in text)

    return codebook, encoded
