from collections import deque


def merge_sort(a):
    """
    Worst-case performance: O(n log n)
    Best-case performance: O(n log n)
    Average performance: O(n log n)

    Returns a new list.
    """
    # transform into a deque so it can be sorted
    a_deque = deque(a)
    # sort
    a_deque_sorted = merge_sort_recursion(a_deque)
    # transform back
    return list(a_deque_sorted)


def merge_sort_recursion(a):
    # base case: one or zero elements are already sorted
    if len(a) <= 1:
        return a

    # copy the left part into another deque
    middle = int(len(a) / 2)
    left = deque()
    for i in range(middle):
        left.append(a.popleft())

    # recursion with left part
    left = merge_sort_recursion(left)

    # recursion right with the remaining
    right = merge_sort_recursion(a)

    # merge the sorted parts
    return merge(left, right)


def merge(left, right):
    merged = deque()

    # while both sides have elements
    while len(left) > 0 and len(right) > 0:
        # if the smallest value from the left side if smaller (or equal) than the smallest value from the right side
        if left[0] <= right[0]:
            # merge the smallest value from the left side
            merged.append(left.popleft())
        # if the smallest value from the right side if smaller than the smallest value from the left side
        else:
            # merge the smallest value from the right side
            merged.append(right.popleft())

    # while the left side has remaining elements
    while len(left) > 0:
        # merge the smallest value from the left side
        merged.append(left.popleft())

    # while the right side has remaining elements
    while len(right) > 0:
        # merge the smallest value from the right side
        merged.append(right.popleft())

    return merged
