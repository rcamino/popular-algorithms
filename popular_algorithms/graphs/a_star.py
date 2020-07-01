import heapq


def a_star(root, transitions, heuristic, callback):
    """
    Worst-case performance: O(b^d) where b="branching factor" and d="search path depth"
    Worst-case space: O(|V|)
    """

    # to indicate if a node was visited
    visited = set()
    # to reconstruct the traversal path
    parent_by_node = dict()

    # just used to break ties with the priority queue
    next_queue_order = 0
    # initialize the priority: use tuples of size 3
    # the first element to compare will be the cost
    # the second element is a tie breaker when costs are the same
    # the third element is the node that will never compared thanks to the second element
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(root), next_queue_order, root))
    next_queue_order += 1

    # to store the current best traversal cost from the root until each node
    # define this before adding to the priority queue
    traversal_cost = {root: 0}

    # while the priority queue is not empty
    while len(priority_queue) > 0:
        # get the node with the smallest priority
        _, queue_order, node = heapq.heappop(priority_queue)

        # ignore nodes that left the queue with a smaller priority
        if node in visited:
            continue

        # mark the node as visited
        visited.add(node)

        # execute the callback with the node
        if callback(node, parent_by_node, traversal_cost):
            # if the callback returns true we stop (can be used for a search)
            return

        # if the node has children
        if node in transitions:
            # for each child
            for child in transitions[node].keys():
                # if the child was not already visited
                if child not in visited:
                    # compute the child cost based on the node cost
                    cost_to_child = traversal_cost[node] + transitions[node][child]

                    # if the child had no cost or this cost is smaller
                    if child not in traversal_cost or cost_to_child < traversal_cost[child]:
                        # assign the parent to reconstruct the path
                        parent_by_node[child] = node
                        # assign the cost from the root
                        traversal_cost[child] = cost_to_child
                        # put the child in the priority queue for the first time
                        # or with a smaller estimated cost than before
                        cost_to_goal_through_child = traversal_cost[child] + heuristic(child)
                        heapq.heappush(priority_queue, (cost_to_goal_through_child, next_queue_order, child))
                        next_queue_order += 1
