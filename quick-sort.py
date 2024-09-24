from random import shuffle
from typing import List


def partition(list: List, start, end):
    i = start
    j = end
    pivotVal = list[start]

    while i < j:
        while list[i] <= pivotVal and i < end:
            i += 1

        # until element <= pivotVal => pivot should be swaped here
        while list[j] > pivotVal and j > start:
            j -= 1

        # no overlap, continue
        if i < j:
            list[i], list[j] = list[j], list[i]
        else:
            break

    # swap pivot to target index (list[j] is the last <= pivotVal element)
    list[start], list[j] = list[j], list[start]

    return j


def quickSort(list: List[int], start, end):
    if start >= end:
        return

    pivot = partition(list, start, end)

    quickSort(list, start, pivot - 1)
    quickSort(list, pivot + 1, end)


def getShuffledList(arr: List) -> List:
    # list(arr) or arr.copy()
    newArr = arr[:]
    shuffle(newArr)
    return newArr


arr = [-10, 1, 2, 5, 11, 10, 9, 10, 100, 3]

for i in range(10):
    randomArr = getShuffledList(arr)
    quickSort(randomArr, 0, len(arr) - 1)
    print(randomArr)



