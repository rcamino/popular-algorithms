from collections import deque


def bfs(root, adjacency_list, callback):
    """
    Worst-case performance: O(|V| + |E|)
    Worst-case space: O(|V|)
    """
    # to indicate if a node was visited
    visited = set()
    # to reconstruct the traversal path
    parent_by_node = dict()

    # initialize the queue with the root
    queue = deque([root])

    # while the queue is not empty
    while len(queue) > 0:
        # get the next in the queue
        node = queue.popleft()
        # mark the node as visited
        visited.add(node)
        # execute the callback with the node
        if callback(node, parent_by_node):
            # if the callback returns true we stop (can be used for a search)
            return

        # if the node has children
        if node in adjacency_list:
            # for each child
            for child in adjacency_list[node]:
                # if the child was not already visited
                if child not in visited:
                    # put the child in the back of the queue
                    queue.append(child)
                    # assign the parent to reconstruct the path
                    parent_by_node[child] = node
