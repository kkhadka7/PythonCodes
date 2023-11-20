from helper import *
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
# plot_digraph(adjacency_list)
# plot_digraph(adjacency_list2, prefix='weighted_digraph')
# plot_graph(adjacency_list)
# plot_graph(adjacency_list2, prefix='weighted_graph')

# adj_list = generate_random_graph(7, 15, directed=False, weighted=False)
adj_list = {'0': ['1', '4', '3', '2'], '1': ['3', '0', '5'], '2': ['4', '3', '0', '5'], '3': ['1', '6', '4', '2', '0'], '4': ['0', '2', '6', '3'], '5': ['6', '1', '2'], '6': ['3', '4', '5']}
print(adj_list)
plot_graph(adj_list)
bfs_order = bfs_traversal(adj_list, '0')
print("BFS order:", bfs_order)
dfs_order = dfs_traversal(adj_list, '0')
print('DFS order:', dfs_order)