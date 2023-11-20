from datetime import datetime
from graphviz import Digraph, Graph

from PIL import Image
import math
import networkx as nx
import random
import matplotlib.pyplot as plt


### Classes
class BinaryNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

### HELPERS
'''
Function to create image for a binary tree in current directory.
prefix can be used to adjust prefix
'''
def visualize_tree(root, prefix="image"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"{prefix}_{timestamp}"
    dot = Digraph(format='png')

    def add_nodes(node):
        if node:
            dot.node(str(node.val))
            if node.left:
                dot.edge(str(node.val), str(node.left.val))
                add_nodes(node.left)
            if node.right:
                dot.edge(str(node.val), str(node.right.val))
                add_nodes(node.right)
    add_nodes(root)
    dot.render(filename, cleanup=True)
    image = Image.open(f"{filename}.png")
    image.show()
    image.close()


def visualize_binary_heap(heap, prefix="binary_heap"):
    #  1   2   3   4   5   6   7   8
    #   \ /     \ /     \ /     \ /
    #    1       2       3       4
    #      \   /           \   /
    #        1               2 
    #            \       /   
    #                1
    gap = 3
    array = heap.array[1:]
    length = len(array)
    if length == 0:
        print("Empty Heap")
        print("=============")
        return
    levels = math.ceil(math.log2(length + 1))
    all_levels = []
    for l in range(levels-1, -1, -1):
        start, end = pow(2, l)-1, pow(2, l+1)-1
        gap = (pow(2, levels+1-l)-1)
        
        space_gap = " " * gap
        nof_els = end - start
        level_elements = array[start:end]
        position = (gap + 2)//2
        level_string = (" " * position) + space_gap.join([str(x) for x in level_elements]) + "\n"
        all_levels.append(level_string)
    max_length = 0
    while all_levels:
        s = all_levels.pop()
        print(s)
        max_length = max(max_length, len(s))
    print("=" * max_length, "\n")

def plot_digraph(adjacency_list, prefix='digraph'):
    '''
    # Example
    adjacency_list = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['D'],
        'D': ['A']
    }

    adjacency_list2 = {
        'A': [('B', -5), ('C', 3)],
        'B': [('A', 5), ('C', 2), ('D', 6)],
        'C': [('D', 1)],
        'D': [('A', 4)]
    }

    create_digraph(adjacency_list)
    create_digraph(adjacency_list2, prefix='weighted_digraph')
    '''
    # Assumption: 
    # if neighbours list is a tuple, it is assumed that second element in the tuple is edge weight.
    is_weighted = all([isinstance(edge, tuple) for neighbor in adjacency_list.values() for edge in neighbor])
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"{prefix}_{timestamp}"

    graph = Digraph(format='png')
    graph.attr('edge', fontcolor='blue', fontsize='12')
    
    for node, neighbors in adjacency_list.items():
        graph.node(node)                
        if is_weighted:
            for neighbor, weight in neighbors:
                graph.edge(node, neighbor, label=str(weight))                
        else:
            for neighbor in neighbors:
                graph.edge(node, neighbor)
    
    # Render and display the graph    
    graph.render(filename, cleanup=True)

def plot_graph(adjacency_list, prefix='graph'):
    '''
    # Examples
    adjacency_list = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['D'],
        'D': ['A']
    }

    adjacency_list2 = {
        'A': [('B', -5), ('C', 3)],
        'B': [('A', 5), ('C', 2), ('D', 6)],
        'C': [('D', 1)],
        'D': [('A', 4)]
    }

    create_graph(adjacency_list)
    create_graph(adjacency_list2, prefix='weighted_graph')
    '''

    # Assumption: 
    # if neighbours list is a tuple, it is assumed that second element in the tuple is edge weight.
    is_weighted = all([isinstance(edge, tuple) for neighbor in adjacency_list.values() for edge in neighbor])
    
    graph = Graph(format='png')
    graph.attr('edge', fontcolor='blue', fontsize='12')
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"{prefix}_{timestamp}"
    added_edges = set()
    
    for node, neighbors in adjacency_list.items():
        graph.node(node)
        for neighbor in neighbors:
            if is_weighted:
                neighbor, weight = neighbor
            if (node, neighbor) not in added_edges and (neighbor, node) not in added_edges:
                if is_weighted: 
                    graph.edge(node, neighbor, label=str(weight))
                else:
                    graph.edge(node, neighbor)
                added_edges.add((node, neighbor))                
    # Render and display the graph
    graph.render(filename, cleanup=True)  

def generate_random_graph(num_nodes, num_edges, directed=False, weighted=False, lower=0, upper=20):
    """
    Generate a random graph and return its adjacency list.

    Parameters:
    - num_nodes: Number of nodes in the graph.
    - num_edges: Number of edges in the graph.
    - directed: If True, create a directed graph. Default is False (undirected).
    - weighted: If True, create weighted edges with weights in the range [1, 20]. Default is False (unweighted).
    - lower: min edge weight to be generated. Default 0
    - upper: max edge weight to be generated. Default 20

    Returns:
    - adjacency_list: A dictionary representing the adjacency list in the specified format.
    """

    # check if num_edges is out of limit
    if num_edges > int(num_nodes*(num_nodes-1) / 2): raise ValueError(f"Number of edges out of bound. Max capacity: {int(num_nodes*(num_nodes-1) / 2)}") 

    G = nx.DiGraph() if directed else nx.Graph()

    # Generate nodes
    nodes = [str(node) for node in range(num_nodes)]
    G.add_nodes_from(nodes)

    if weighted:
        # Generate weighted edges
        while G.number_of_edges() < num_edges:
            source = str(random.randint(0, num_nodes - 1))
            target = str(random.randint(0, num_nodes - 1))
            weight = random.randint(lower, upper)
            if source != target and not G.has_edge(source, target):
                G.add_edge(source, target, weight=weight)
    else:
        # Generate unweighted edges
        possible_edges = [(source, target) for source in G.nodes() for target in G.nodes() if source != target]
        random.shuffle(possible_edges)
        for i in range(min(num_edges, len(possible_edges))):
            source, target = possible_edges[i]
            G.add_edge(source, target)

    adjacency_list = {}

    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        if weighted:
            neighbor_data = [(neighbor, G[node][neighbor]['weight']) for neighbor in neighbors]
        else:
            neighbor_data = neighbors
        adjacency_list[node] = neighbor_data

    return adjacency_list


def bfs_traversal(adj_list, start_node):
    queue = list()
    visited = list()
    queue.append(start_node)
    while queue:
        current_node = queue.pop(0)
        if not current_node in visited:
            visited.append(current_node)
            for neighbor in adj_list[current_node]:
                queue.append(neighbor)
    return visited

def dfs_traversal(adj_list, start_node):
    visited = list()
    stack = list()
    stack.append(start_node)
    while stack:
        current_node = stack.pop()
        if not current_node in visited:
            visited.append(current_node)
            for neighbor in adj_list[current_node]:
                stack.append(neighbor)
    return visited