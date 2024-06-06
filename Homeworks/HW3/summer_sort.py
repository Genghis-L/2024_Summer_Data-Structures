import random

'''
What is the best-case runtime complexity of SummerSort?
Answer: TODO
What is the worst-case runtime complexity of SummerSort?
Answer: TODO
'''

def find_max(array, a, b):
    """ Finds the position of the largest element between two indices in the array.
        @array: the python list
        @a:     the index of first element to check
        @b:     the index of last element to check

        return: index of the largest element
    """
    maxPos = a
    for i in range(a, b):
        if (array[maxPos] < array[i]):
            maxPos = i
    return maxPos


def reverse(array, a, b):
    """ Reverses the elements between two indices in the array.
        @array: the python list
        @a:     the index of first element to reverse
        @b:     the index of "one past" last element to reverse
    """
    l = a
    r = b
    while (l < r):
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1


def summer_sort(array):
    """ Sorts the array using find_max(array, a, b) and reverse(array, a, b) functions.
        @array: the python list
    """
    # To do
    pass


def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))

    print("Before sorting:")
    print(array)
    summer_sort(array)
    print("After sorting:")
    print(array)


if __name__ == "__main__":
    main()