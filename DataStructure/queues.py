import queue

data_queue = queue.Queue()

data_queue.put('funcoding')
data_queue.put(1)

print(data_queue.qsize())   # 2
print(data_queue.get())     # 'funcoding'
print(data_queue.qsize())   # 1


data_lifoQueue = queue.LifoQueue()

data_queue.put('funcoding')
data_queue.put(1)
print(data_queue.get())    # 1


data_priorityQueue = queue.PriorityQueue()

data_priorityQueue.put((10, 'korea'))
data_priorityQueue.put((5, 1))
data_priorityQueue.put((15, 'china'))

print(data_priorityQueue.qsize())   # 3
print(data_priorityQueue.get())     # (5, 1)
print(data_priorityQueue.get())     # (10, 'korea)