
def countingSort(a: list) -> list:
    minVal: int = min(a)
    valueRange: int = max(a) - minVal + 1

    counter: list = [0] * valueRange

    # count for element
    for item in a:
        counter[item - minVal] += 1

    for index, val in enumerate(counter):
        if index == 0:
            continue
        # counter prefix sum => last element is total count == len(a)
        counter[index] = val + counter[index - 1]

    result: list = [None] * len(a)

    # loop a, better then loop counter, but prefix sum required

    # to right, unstable
    for value in a:

        # to left, stable
        # for index in range(len(a) - 1, -1, -1):
        #     value = a[index]
        # find index, place the element
        result[counter[value - minVal] - 1] = value
        # prefix sum - 1
        counter[value - minVal] -= 1

    return result


def countingSort2(a: list) -> list:
    minVal: int = min(a)
    valueRange: int = max(a) - minVal + 1

    counter: list = [0] * valueRange

    # count for element
    for item in a:
        # absolute value
        counter[item - minVal] += 1

    result: list = [None] * len(a)
    i = 0

    # loop counter - no need for prefix sum
    for val, count in enumerate(counter):
        # restore val by + minVal
        cnt = count

        while cnt > 0:
            result[i] = val + minVal
            i += 1
            cnt -= 1

    return result


print(countingSort([652, 721, 177, 977, 24, 17, 126, 515, 442, 917]))
print(countingSort2([652, 721, 177, 977, 24, 17, 126, 515, 442, 917]))
print(countingSort([5, 3, 5, 4, 10, 3]))
print(countingSort2([5, 3, 5, 4, 10, 3]))
