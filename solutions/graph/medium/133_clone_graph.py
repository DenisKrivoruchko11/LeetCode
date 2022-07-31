from queue import Queue

# Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the
# graph. Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node) -> Node:
    nodes, q = {node.val: Node(node.val)}, Queue()
    q.put(node)
    while not q.empty():
        cur = q.get()
        for n in cur.neighbors:
            if n.val not in nodes:
                nodes[n.val] = Node(n.val)
                q.put(n)
            nodes[cur.val].neighbors.append(nodes[n.val])
    return nodes[node.val]
