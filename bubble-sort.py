from typing import List


def bubble_sort(list: List[int]) -> List[int]:
    length = len(list)
    flag = False

    for i in range(0, length):
        if flag:
            break

        # mark as no change any more
        flag = True

        j = length - 1

        while j > i:
            # from right to left, min value bubbles to i => i = j - 1
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
                flag = False

            j -= 1

    return list


def bubble_sort2(list: List[int]) -> List[int]:
    length = len(list)
    flag = False

    for i in range(0, length):
        if flag:
            break

        # mark as no change any more
        flag = True

        j = 0

        # marginal case:
        #   when i == 0, j(max) == length - 1 - 1: 
        #       j(max) + 1 = length - 1, not out of range
        while j < length - 1 - i:
            # from left to right, max value bubbles to => j = length - 1 - i
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                flag = False

            j += 1

        print(list)
    return list


print(bubble_sort([1, 101, -3, 4, 100, 8]))
print(bubble_sort2([1, 101, -3, 4, 100, 8]))
print(bubble_sort([1, 101, -3, 4, 100, 8]) ==
      bubble_sort2([1, 101, -3, 4, 100, 8]))

# is operator means identical
# == on collections means every element is same
