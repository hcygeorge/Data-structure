from collections import deque

# doubled-end queue
q = deque([5, 6, 7])

print(q)
while q:
    print(q.pop())
print(q)

# popleft
q = deque([5, 6, 7])
while q:
    print(q.popleft())


q = deque([])
for i in range(3):
    q.append(i)
    
print(q)