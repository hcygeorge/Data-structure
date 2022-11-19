# sort(), sorted()

## Time complexity: O(nlogn)
Python的sort,sorted使用Timsort，是一種混合merge sort和insertion sort的排序算法，Timsort的時間複雜度最好有O(n)，最糟也有O(nlogn)。

> 補充: Java的sort也是採用Timsort

## 範例
```python
list1 = [20, 5, -10, 300]
list1.sort(reverse=True) # Sort the list in descending order

# A callable function which returns the length of a string
def lengthKey(str):
  return len(str)

list2 = ["London", "Paris", "Copenhagen", "Melbourne"]
# Sort based on the length of the elements
list2.sort(key=lengthKey)
print(list2)
```

## Refernence
https://www.geeksforgeeks.org/timsort/