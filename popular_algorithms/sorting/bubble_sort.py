def bubble_sort(a):
    """
    Worst-case performance: O(n^2)
    Best-case performance: O(n) when the list is sorted
    Average performance: O(n^2)

    In place. Returns the input.
    """
    # count how many are sorted already (the last n)
    for n in range(len(a)):
        # for the best case
        swaps_made = False

        # we will compare two elements at the time
        # the current with the next one
        # start from the beginning but ignore the last that are already sorted
        for i in range(len(a) - n - 1):
            # if the current element is bigger than the next one
            if a[i] > a[i + 1]:
                # swap them (bubble up the biggest element)
                a[i], a[i + 1] = a[i + 1], a[i]
                # this is not the best case
                swaps_made = True

        # best case: if nothing changed then nothing will change on next iteration
        if not swaps_made:
            # so we can stop now
            break
    return a
