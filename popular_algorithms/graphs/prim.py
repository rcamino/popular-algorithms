import heapq


def minimum_spanning_tree(nodes, transitions):
    """
    Worst-case performance: O(|E| log |V|)
    Worst-case space: O(|V| + |E|)
    """
    tree_edges = []
    edge_to_parent = dict()
    node_in_tree = {node: False for node in nodes}
    best_cost = dict()
    priority_queue = []
    priority_queue_order = 0

    # take any node as root
    root = next(iter(nodes))

    # start with the root in the priority queue
    best_cost[root] = 0
    heapq.heappush(priority_queue, (0, priority_queue_order, root))
    priority_queue_order += 1

    while len(priority_queue) > 0:
        # get the next node ordered by key
        _, _, node = heapq.heappop(priority_queue)

        # this was already selected with a better priority
        if node_in_tree[node]:
            continue

        # add the node to the tree
        node_in_tree[node] = True
        # if it is not the root node
        if node in edge_to_parent:
            # add to the tree the edge that links the node to the parent
            tree_edges.append(edge_to_parent[node])

        for child, cost in transitions[node].items():
            # if the child is not in the tree
            # and the child has no best cost or if the edge with the node has a better cost
            if not node_in_tree[child] and (child not in best_cost or best_cost[child] > cost):
                # update the key
                best_cost[child] = cost
                # put in the queue with the key as priority level
                heapq.heappush(priority_queue, (cost, priority_queue_order, child))
                priority_queue_order += 1
                # indicate which edge was used
                edge_to_parent[child] = (node, child, cost)

    return tree_edges
