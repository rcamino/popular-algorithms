def floyd_warshall(nodes, edges):
    """
    Worst-case performance: O(|V|^3)
    Worst-case space: O(|V|^2)
    """
    # to store the current best traversal cost between node pairs
    costs = {}

    # initialize best traversal between node pairs that have edges between them
    for source, target, cost in edges:
        costs[(source, target)] = cost

    # define no cost from a node to itself
    for node in nodes:
        costs[(node, node)] = 0

    # for each node in the middle
    for middle in nodes:
        # for each source
        for source in nodes:
            # and each target
            for target in nodes:
                # if the traversal cannot be split in the middle do not continue
                if (source, middle) not in costs or (middle, target) not in costs:
                    continue

                # if there is no direct traversal between source and target
                # or if splitting the traversal in the middle has lower cost
                if (source, target) not in costs or \
                        costs[(source, target)] > costs[(source, middle)] + costs[(middle, target)]:
                    costs[(source, target)] = costs[(source, middle)] + costs[(middle, target)]

    # return all the traversal costs
    return costs
