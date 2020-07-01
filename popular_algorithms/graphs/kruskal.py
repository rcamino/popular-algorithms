from operator import itemgetter


def minimum_spanning_tree(nodes, edges):
    """
    Worst-case performance: O(|E| log |E|)
    Worst-case space: O(|E|)
    """

    # sort edges by the cost
    # it is the third element from (source, target, cost)
    sorted_edges = sorted(edges, key=itemgetter(2))

    # initialization
    parent_by_node = dict()
    rank_by_node = dict()
    for node in nodes:
        # each node starts as the root of its own set
        parent_by_node[node] = node
        # all the sets have rank 0
        rank_by_node[node] = 0

    # the spanning tree has |E| = |V| - 1
    tree_edges = []
    next_edge = 0
    while len(tree_edges) < len(nodes) - 1:
        # pick the next edge sorted by cost
        edge = sorted_edges[next_edge]
        # increase the pointer to the sorted edges
        next_edge += 1
        # extract the extremes to make it easier
        source, target, _ = edge
        # find the roots of both extremes
        source_root = find(source, parent_by_node)
        target_root = find(target, parent_by_node)
        # if both nodes don't share the root
        if source_root != target_root:
            # add the edge to the tree
            tree_edges.append(edge)
            # union of both sets
            union(source_root, target_root, rank_by_node, parent_by_node)

    # just return the edge list
    return tree_edges


def find(node, parent_by_node):
    parent = parent_by_node[node]
    # when a node is its own parent then it is the root of the tree
    if node == parent:
        return node
    # if not follow the parent to continue searching for the root
    return find(parent, parent_by_node)


def union(root_a, root_b, rank_by_node, parent_by_node):
    # if one tree is smaller than the other one
    # attach the smaller one to the root of the taller one
    # so the merged tree does not grow in height
    # the rank of the smaller one does not matter anymore because it won't be checked again

    # if tree a is shorter than tree b
    if rank_by_node[root_a] < rank_by_node[root_b]:
        # attach tree a to the root of tree b
        parent_by_node[root_a] = root_b
    # if tree b is shorter than tree a
    elif rank_by_node[root_a] > rank_by_node[root_b]:
        # attach tree b to the root of tree a
        parent_by_node[root_b] = root_a
    # if they have the same height
    else:
        # attach tree b to the root of tree a (arbitrary)
        parent_by_node[root_b] = root_a
        # but now the height of a increases
        rank_by_node[root_a] += 1
