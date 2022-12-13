# Linked list

- Linked list使用node記錄資料和位置的結構，每個節點都有data和pointer
- 若是單向，則只有一個pointer next，雙向則有next和prev兩個pointer
- 第一個節點稱為head
- 最後一個節點pointer指向None

## 類別

```python
# define a linked list node
class ListNode:
    """A node of linked list."""
    def __init__(self, x):
        self.val = x
        self.next = None  # point to next node

# iterate through a linked list
ite = head
while ite:
    print(ite.val)
    ite = ite.next
```



## 適用範圍
- 不在意單點資料存取(不用random access)
- 希望新增資料的成本降低(不用resize array)
- 要找的資料剛好靠近頭或尾(因為搜尋是O(n))


## 參考
https://hiskio.com/courses/319/lectures/15386