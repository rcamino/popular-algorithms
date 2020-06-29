def insertion_sort(a):
    """
    Worst-case performance: O(n^2)
    Best-case performance: O(n) when the list is sorted
    Average performance: O(n^2)

    In place. Returns the input.
    """
    # grow a sorted list by inserting the next element in the right position
    # skip the first case where the first element can only be inserted in the first position
    for n in range(1, len(a)):
        # go backwards from the current element
        # until the second one
        # swapping the current element with the previous one
        # until we find where to insert the current element
        i = n
        while i > 0 and a[i] < a[i - 1]:
            # swap with the previous one
            a[i], a[i - 1] = a[i - 1], a[i]
            # go backwards
            i -= 1
    return a
