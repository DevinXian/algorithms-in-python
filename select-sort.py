
from typing import List


def select_sort(list: List[int]) -> List[int]:
    length = len(list)

    for i in range(0, length - 1):
        # min value index
        index = i

        for j in range(i + 1, length):
            if list[j] < list[index]:
                index = j

        if index != i:
            list[index], list[i] = list[i], list[index]

    return list


print(select_sort([1, 101, -3, 4, 100, 8]))
print(select_sort([1]))
print(select_sort([]))
