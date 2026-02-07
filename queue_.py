from collections import deque                                #header
my_queue = deque()
my_queue.append(1)
my_queue.appendleft(2)
print(my_queue)
my_queue.popleft()
print(my_queue)