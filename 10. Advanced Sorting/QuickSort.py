def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def medianOfThree(array, a, b):
    global comparisons, swaps

    mid = (a + b) // 2

    # Order array[a], array[b] and array[mid]
    if array[a] > array[mid]:
        swap(array, a, mid)
        swaps += 1
    if array[a] > array[b]:
        swap(array, a, b)
        swaps += 1
    if array[mid] > array[b]:
        swap(array, mid, b)
        swaps += 1

    comparisons += 3

    # Swap the median value to the end: array[b]
    swap(array, mid, b)


def inplace_quick_sort(array, a, b):
    global comparisons, swaps

    # Base Case: If there is only one elmt, no need to swap
    if a >= b:
        return

    # Use median of three method to find pivot and put it to the array end: array[b]
    medianOfThree(array, a, b)
    pivot = array[b]
    i = a  # left pointer
    j = b - 1  # right pointer

    while True:
        # while until we find the two elmts need to be swapped
        while i <= j:
            comparisons += 1
            if array[i] >= pivot:
                break
            i += 1
        while i <= j:
            comparisons += 1
            if array[j] <= pivot:
                break
            j -= 1

        if i <= j:
            # If these two elmts are valid to swap
            swap(array, i, j)
            swaps += 1
            i += 1
            j -= 1
        else:
            # Otherwise, we break the outer while and proceed
            break

    # swap the left pointer and the pivot
    swap(array, i, b)
    swaps += 1
    # one partition is done, pivot is now at correct position

    # Do recursion on the left and the right side
    inplace_quick_sort(array, a, i - 1)
    inplace_quick_sort(array, i + 1, b)


def quick_sort(array):
    """Do the quick sort and return (comparisons, swaps)"""
    global comparisons, swaps
    comparisons, swaps = 0, 0
    inplace_quick_sort(array, 0, len(array) - 1)
    return comparisons, swaps
