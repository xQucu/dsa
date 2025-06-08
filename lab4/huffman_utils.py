class MinHeap():
    def __init__(self):
        self.data: list[tuple[int, any]] = [0] * 10000
        self.length = 0

    def insert(self, value):
        self.data[self.length] = value
        self._heapifyUp(self.length)
        self.length += 1

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


# def huffman_coding(text: str):
#     counter = {}
#     for c in text:
#         if c in counter:
#             counter[c] += 1
#         else:
#             counter[c] = 1
#             heap = MinHeap()
