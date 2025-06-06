import math


class MinHeap():
    def __init__(self):
        self.data = [None] * 1000
        self.length = 0

    def insert(self, value):
        self.data[self.length] = value
        self._heapifyUp(self.length)
        self.length += 1

    def delete(self):
        if self.length == 0:
            # raise ValueError("Can't delete from empty heap")
            return None

        out = self.data[0]
        self.length -= 1

        if self.length == 0:
            self.data = []
            return out

        self.data[0] = self.data[self.length]
        self._heapifyDown(0)
        return out

    def _heapifyDown(self, idx: int) -> None:
        lIdx = self._leftChild(idx)
        rIdx = self._rightChild(idx)

        if idx >= self.length or lIdx >= self.length:
            return

        lV = self.data[lIdx]
        rV = self.data[rIdx]
        v = self.data[idx]

        if lV > rV and v > rV:
            self.data[idx] = rV
            self.data[rIdx] = v
            self._heapifyDown(rIdx)
        elif rV > lV and v > lV:
            self.data[idx] = lV
            self.data[lIdx] = v
            self._heapifyDown(lIdx)
        elif lV == rV and v > rV:
            p = self._parent(idx)
            parentV = self.data[p]

            self.data[rIdx] = parentV
            self.data[p] = rV
            self._heapifyDown(p)

    def _heapifyUp(self, idx: int) -> None:
        if (idx == 0):
            return

        p = self._parent(idx)
        parentV = self.data[p]
        v = self.data[idx]

        if parentV > v:
            self.data[idx] = parentV
            self.data[p] = v
            self._heapifyUp(p)

    def _parent(self, idx: int) -> int:
        return math.floor((idx-1)/2)

    def _leftChild(self, idx: int) -> int:
        return (idx * 2 + 1)

    def _rightChild(self, idx: int) -> int:
        return (idx * 2 + 2)


def huffman_coding(text: str):
    counter = {}
    for c in text:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    


huffman_coding("lossless")
