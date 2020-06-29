def selection_sort(a):
    """
    Worst-case performance: O(n^2)
    Best-case performance: O(n^2)
    Average performance: O(n^2)

    In place. Returns the input.
    """
    # count how many are sorted already (the first n)
    for n in range(len(a)):
        # assume that the first unsorted element is the minimum
        min_i = n

        # check the next unsorted elements
        # and select the minimum
        for i in range(n + 1, len(a)):
            # if the current unsorted element is the minimum
            if a[i] < a[min_i]:
                # update the minimum
                min_i = i

        # if the minimum was no the first unsorted element
        if min_i != n:
            # swap them
            a[n], a[min_i] = a[min_i], a[n]
    return a
