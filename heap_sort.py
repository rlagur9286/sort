class HeapSort:
    def __init__(self, arr):
        self.heapify(arr, len(arr))

    def heapify(self, arr, size):
        idx = int(size / 2) - 1
        while idx >= 0:
            self.siftdown(arr, idx, size)
            idx -= 1

    def siftdown(self, arr, idx, size):
        left = 2 * idx + 1
        right = 2 * idx + 2
        large_idx = idx

        if left <= size - 1 and arr[idx] < arr[left]:
            large_idx = left
        if right <= size - 1 and arr[large_idx] < arr[right]:
            large_idx = right

        if large_idx != idx:
            self.swap(arr, large_idx, idx)
            self.siftdown(arr, large_idx, size)

    def swap(self, arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]

    def do_sort(self, arr, size):
        end = size - 1
        while end > 0:
            self.swap(arr, 0, end)
            self.siftdown(arr, 0, end)
            end -= 1

arr = [7, 2, 5, 4, 1, 6 ,3]
heap = HeapSort(arr)
print(arr)
heap.do_sort(arr, len(arr))
print(arr)