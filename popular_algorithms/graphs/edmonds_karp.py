from collections import deque


def maximum_flow(flow_source, flow_target, capacities):
    """
    Worst-case performance: O(|V||E|^2)
    Worst-case space: O(|V| + |E|) |V| used on each bfs and |E| to keep the residuals
    """
    # copy the capacities to use as residuals
    # the residuals will be modified
    residuals = dict()
    for node_source, capacity_by_target in capacities.items():
        residuals[node_source] = dict()
        for node_target, capacity in capacity_by_target.items():
            residuals[node_source][node_target] = capacity

    # initial flow
    max_flow = 0

    # initial run
    reached_target, parent_by_node = flow_bfs(flow_source, flow_target, residuals)
    # if the target is still reachable
    while reached_target:
        # flow initial value
        path_flow = float("Inf")
        # start from the target
        node = flow_target
        # until we reach the source
        while node != flow_source:
            # get the previous step
            parent = parent_by_node[node]
            # the flow is limited be the edge
            path_flow = min(path_flow, residuals[parent][node])
            # continue backwards
            node = parent

        # add the flow of the path
        max_flow += path_flow

        # start updating the residuals from the target
        node = flow_target
        # until we reach the source
        while node != flow_source:
            # get the previous step
            parent = parent_by_node[node]
            # the edge has more flow so the residual or remaining capacity is reduced
            residuals[parent][node] -= path_flow
            # continue backwards
            node = parent

        # next iteration (with new residuals)
        reached_target, parent_by_node = flow_bfs(flow_source, flow_target, residuals)

    return max_flow


def flow_bfs(flow_source, flow_target, residuals):
    # to indicate if a node was visited
    visited = set()
    # to reconstruct the traversal path
    parent_by_node = dict()

    # initialize the queue with the source
    queue = deque([flow_source])

    # while the queue is not empty
    while len(queue) > 0:
        # get the next in the queue
        node = queue.popleft()
        # mark the node as visited
        visited.add(node)
        # if we reach the target
        if node == flow_target:
            # we finish
            return True, parent_by_node

        # if the node has children
        if node in residuals:
            # for each child with residual
            for child, residual in residuals[node].items():
                # if the child was not already visited and has residual
                if child not in visited and residual > 0:
                    # put the child in the back of the queue
                    queue.append(child)
                    # assign the parent to reconstruct the path
                    parent_by_node[child] = node

    # the target was not reached
    return False, None
