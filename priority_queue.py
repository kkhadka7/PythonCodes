import heapq
import queue
# Create an empty priority queue
priority_queue = []

# Add elements to the priority queue
heapq.heappush(priority_queue, 3)
heapq.heappush(priority_queue, 1)
heapq.heappush(priority_queue, 2)

# Retrieve and remove the element with the highest priority
highest_priority = heapq.heappop(priority_queue)
print("Highest Priority:", highest_priority)

# Add a new element and pop the highest priority in a single operation
new_element = 4
highest_priority = heapq.heappushpop(priority_queue, new_element)
print("New Highest Priority:", highest_priority)

# Display the current element with the highest priority (without removing it)
current_highest_priority = priority_queue[0]
print("Current Highest Priority:", current_highest_priority)

# Convert an existing list into a priority queue
my_list = [5, 2, 7, 1, 9]
heapq.heapify(my_list)
print("Priority Queue from Existing List:", my_list)


my_queue = queue.Queue()
my_pq = queue.PriorityQueue()
my_stack = queue.LifoQueue()

import threading
import queue

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()

# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()

# Send thirty task requests to the worker.
for item in range(30):
    q.put(item)

# Block until all tasks are done.
q.join()
print('All work completed')