from PriorityQueue import *

pq = PriorityQueue(5)
pq.insert(5)
pq.insert(2)
pq.insert(4)
pq.insert(3)
pq.insert(1)
print(pq)
print(pq.remove())
print(pq)
print(pq.peek())
print(len(pq))
print(pq.isFull())
print(pq.isEmpty())