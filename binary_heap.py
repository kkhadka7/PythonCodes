from helper import visualize_binary_heap

class BinaryMaxHeap:
    def __init__(self):
        self.array = [0]
    
    def insert(self, value):
        if not self.array:
            self.array.append(value)
        else:
            self.array.append(value)
            index = len(self.array)-1
            
            while index > 1:
                parent = index // 2
                if self.array[parent] < value: # change to > for Min heap
                    temp = self.array[parent]
                    self.array[parent] = value
                    self.array[index] = temp
                index = parent
    
    def remove(self):
        length = len(self.array)
        if length == 1:
            raise Exception("Can't extract from empty heap.")
        elif length == 2:
            return self.array.pop()
        # 
        last_el = self.array.pop()
        result = self.array[1]
        self.array[1] =  last_el

        head = 1
        child = 2 * head
        visualize_binary_heap(self)
        # while at least left child is within the array
        while child < len(self.array):
            # if right child is within the array and right child is greater than left child.
            if child + 1 < len(self.array) and self.array[child + 1] > self.array[child]:
                child += 1
            if self.array[head] < self.array[child]:
                self.array[head], self.array[child] = self.array[child], self.array[head]
                head = child
                child = 2 * head
            visualize_binary_heap(self)
        return result

if __name__=="__main__":
    myheap = BinaryMaxHeap()
    array = [10, 20, 30, 25, 5, 40, 35, 12]
    for el in array:
        myheap.insert(el)
    visualize_binary_heap(myheap)
    
    while myheap.array:
        print(myheap.remove())
        visualize_binary_heap(myheap)





