def bellman_ford(root, nodes, edges):
    """
    Worst-case performance: O(|V||E|)
    Worst-case space: O(|V|)
    """
    # to reconstruct the traversal path
    parent_by_node = dict()

    # to store the current best traversal cost from the root until each node
    traversal_cost = {root: 0}

    # repeat once per node
    # on each iteration paths of incremental depth will be analyzed
    for _ in range(len(nodes)):
        # go through all the edges
        for source, target, cost in edges:
            # if the source has no best path defined do not check the rest
            if source not in traversal_cost:
                continue

            # if the target node has no best path defined
            # or if it is better to reach the target node going through the source code
            # than using the current best path
            if target not in traversal_cost or traversal_cost[source] + cost < traversal_cost[target]:
                traversal_cost[target] = traversal_cost[source] + cost
                parent_by_node[target] = source

    # go through all the edges
    for source, target, cost in edges:
        # if this happens then there is a negative cycle
        if source in traversal_cost and target in traversal_cost \
                and traversal_cost[source] + cost < traversal_cost[target]:
            raise Exception("Negative cycle detected.")

    # return all the traversal costs and parents
    return traversal_cost, parent_by_node
