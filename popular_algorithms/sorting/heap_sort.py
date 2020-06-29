from math import floor


def heap_sort(a):
    """
    Worst-case performance: O(n log n)
    Best-case performance: O(n log n)
    Average performance: O(n log n)

    In place. Returns the input.
    """
    # build the heap with the largest element at the top (max-heap)
    heapify(a)

    # this indicates where to put the next max element of the heap
    # we start at the end of the list
    end = len(a) - 1
    # while the back part of the list does not reach the front
    while end > 0:
        # swap the max element of the heap with the limit of the back of the list
        a[end], a[0] = a[0], a[end]
        # move backwards the limit of the back of the list
        # (grow the back of the list and shrink the heap)
        end -= 1
        # repair the heap without considering the back of the list
        repair_heap(a, 0, end)
    return a


def heapify(a):
    # the last element
    last = len(a) - 1
    # the start is the parent of the last element
    start = parent_of(last)
    # until the fixing reaches the root
    while start >= 0:
        # fix the subtree
        repair_heap(a, start, last)
        # go backwards
        start -= 1


def repair_heap(a, start, end):
    # initial pointers
    root = start
    left = left_of(root)
    right = left + 1

    # while there is a left child
    while left <= end:
        # initially the root is the largest
        max_node = root

        # if the left child is larger
        if a[left] > a[max_node]:
            max_node = left

        # if there is a right child and it is larger
        if right <= end and a[right] > a[max_node]:
            max_node = right

        # if the root is still the max node
        if max_node == root:
            # there is nothing else to do
            return
        # if the root is not the max node
        else:
            # swap the root
            a[root], a[max_node] = a[max_node], a[root]
            # update pointers
            root = max_node
            left = left_of(root)
            right = left + 1


def parent_of(i):
    return floor((i - 1) / 2)


def left_of(i):
    return 2 * i + 1


def right_of(i):
    return 2 * i + 2
