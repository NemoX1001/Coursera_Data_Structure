# python3

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        self.n = n
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def GenerateSwaps(self):
        self.RepairHeap()

    def RepairHeap(self):
        for i in range(int(self.n / 2), -1, -1):
            self.SiftDown(i)

    def Parent(self, i):
        return self._data[int((i-1)/2)]

    def LeftChild(self, i):
        return 2 * i + 1

    def RightChild(self, i):
        return 2 * i + 2

    def SiftDown(self, i):
        minIndex = i
        left = self.LeftChild(i)
        if left < self.n and self._data[left] < self._data[minIndex]:
            minIndex = left

        right = self.RightChild(i)
        if right < self.n and self._data[right] < self._data[minIndex]:
            minIndex = right
        if i != minIndex:
            self._swaps.append((i, minIndex))
            self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
            self.SiftDown(minIndex)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()