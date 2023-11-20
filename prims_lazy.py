from helper import *
import queue
import random

# graph_al = generate_random_graph(5, 7, weighted=True, upper=15)
# plot_graph(graph_al)
# graph_al = {'0': [('1', 15), ('4', 6), ('2', 8)], '1': [('3', 11), ('4', 4), ('0', 15)], '2': [('3', 15), ('0', 8), ('4', 5)], '3': [('1', 11), ('2', 15)], '4': [('1', 4), ('0', 6), ('2', 5)]}
graph_al = {
    'A': [('F', 5), ('B', 25)],
    'B': [('A', 25), ('C', 9), ('G', 6)],
    'C': [('B',9),('D', 10)],
    'D': [('C', 10), ('E', 12), ('G', 11)],
    'E': [('D', 12), ('F', 18), ('G', 16)],
    'F': [('A', 5), ('E', 18)],
    'G': [('B', 6), ('D', 11), ('E', 16)]
}
print('Graph:', graph_al)
plot_graph(graph_al)

# Initialize variables
# MST as a hashset
mst = {} # { start_node: [(end_node, edge_weight)] }
# visited set contains all the nodes already visited and are added in MST.
visited = set()
mst_cost = 0
priority_queue = queue.PriorityQueue()
# start_node = next(iter(graph_al)) # always first key
start_node = random.choice(list(graph_al.keys())) # random key


for adj_node, edge_weight in graph_al[start_node]:
    priority_queue.put((edge_weight, adj_node, start_node)) # (edge_weight, end_node, start_node)
    # print(list(priority_queue.queue)) # prints the items in priority queue as a list
visited.add(start_node)
while not priority_queue.empty():
    min_cost, min_adj_node, start_node = priority_queue.get()
    #  print(start_node, min_adj_node, min_cost, list(priority_queue.queue))
    if not min_adj_node in visited:
        visited.add(min_adj_node)
        # print(visited)
        mst_cost += min_cost
        if not start_node in mst.keys():
            mst[start_node] = [(min_adj_node, min_cost)]
        else:
            mst[start_node].append((min_adj_node, min_cost))
        for adj_node, edge_weight in graph_al[min_adj_node]:
            priority_queue.put((edge_weight, adj_node, min_adj_node))


print(mst_cost)
print(mst)
plot_graph(mst)







