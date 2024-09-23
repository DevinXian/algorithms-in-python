from typing import List

def insert_sort(list: List[int]) -> List[int]:
    length = len(list)

    for pos in range(1, length):
        # pick one elment to insert
        val = list[pos]
        # current index
        index = pos

        # is left element bigger than val
        while list[index - 1] > val and index > 0:
            # move to right
            list[index] = list[index - 1]
            index -= 1

        list[index] = val

    return list

def insert_sort2(list):
    length = len(list)

    for pos in range(1, length):
        # pick one elment to insert
        val = list[pos]
        # left index
        index = pos - 1

        # is left element bigger than val
        while list[index] > val and index >= 0:
            # move to right
            list[index + 1] = list[index]
            index -= 1

        # current
        list[index + 1] = val

    return list

print(insert_sort([1, 101, -3, 4, 100, 8]))
print(insert_sort2([1, 101, -3, 4, 100, 8]))
