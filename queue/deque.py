# deque
# 雙端佇列（double-ended queue，通常縮寫為 deque）是一般化（generalize）的佇列或堆疊。
# 比起佇列只能「先進先出 FIFO」，以及堆疊只有「後進先出 LIFO」，
# 雙端佇列可以從最前端或最末端任意方向，在常數時間複雜度內增刪元素，更為方便。
from collections import deque

# doubled-end queue(頭尾兩邊都能取出元素)
q = deque([5, 6, 7])
print('a', q)

# pop從右邊取，等於先進後出
while q:
    print('b', q.pop())

# popleft從左邊取，等於先進先出
q = deque([5, 6, 7])
while q:
    print('c', q.popleft())


q = deque([])
for i in range(3):
    q.append(i)
    
print(q)