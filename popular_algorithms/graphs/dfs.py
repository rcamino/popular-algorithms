from collections import deque


def dfs(root, adjacency_list, callback):
    """
    Worst-case performance: O(|V| + |E|)
    Worst-case space: O(|V|)
    """

    # to indicate if a node was visited
    visited = set()
    # to reconstruct the traversal path
    parent_by_node = dict()

    # initialize the stack with the root
    stack = deque([root])

    # while the stack is not empty
    while len(stack) > 0:
        # get the top of the stack
        node = stack.popleft()
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
                    # put the child in the top of the stack
                    stack.appendleft(child)
                    # assign the parent to reconstruct the path
                    parent_by_node[child] = node
