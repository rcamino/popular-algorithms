def quick_sort(a):
    """
    Worst-case performance: O(n^2) when the pivot does not divide the partition in two
    Best-case performance: O(n log n) when each side of the partition is equally big
    Average performance: O(n log n) when each side of the partition has almost the same size

    In place. Returns the input.
    """
    return quick_sort_recursion(a, 0, len(a) - 1)


def quick_sort_recursion(a, start, end):
    # if the limits are valid (sizes 0 and 1 are sorted by definition)
    if start < end:
        # chose a pivot
        # put it on the final position
        # the smaller to the left and the larger to the right
        pivot = partition(a, start, end)
        # sort left part
        quick_sort_recursion(a, start, pivot - 1)
        # sort right part
        quick_sort_recursion(a, pivot + 1, end)

    return a


def partition(a, start, end):
    # chose the last element as the pivot
    pivot = a[end]
    # keep the position where to put the next value that is smallest than the pivot
    smallest = start
    # check one element at the time not including the last which is the pivot
    for current in range(start, end):
        # if the current element is smallest than the pivot
        if a[current] < pivot:
            # put the current element in the available position
            a[smallest], a[current] = a[current], a[smallest]
            # move to the next available position
            smallest += 1

    # swap the pivot to the next available position
    a[smallest], a[end] = a[end], a[smallest]
    return smallest
