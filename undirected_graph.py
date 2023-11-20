from graphviz import Digraph

# Sample adjacency list for a directed graph with edge weights
adjacency_list = {
    'A': [('B', 5), ('C', 3)],
    'B': [('C', 2), ('D', 7)],
    'C': [('D', 1)],
    'D': [('A', 4)]
}

# Create a Graphviz digraph
digraph = Digraph(format='png')

for node, neighbors in adjacency_list.items():
    digraph.node(node)
    for neighbor, weight in neighbors:
        digraph.edge(node, neighbor, label=str(weight))
        if weight < 5:
            # Set the font color and size for labels based on the weight
            digraph.attr('edge', fontcolor='red', fontsize='10')
        else:
            digraph.attr('edge', fontcolor='blue', fontsize='12')

# Render and display the directed graph with customized edge label colors and sizes
digraph.render('weighted_digraph')  # This will save the graph as 'weighted_digraph.pdf'
digraph.view('weighted_digraph')    # This will open the graph in a viewer
