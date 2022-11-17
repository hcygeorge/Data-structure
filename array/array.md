# Array
- 通常會建立變數length記錄刪除後實際的元素個數，每次迭代增減元素後，length要跟著變動

## Insert
- 插入通常需要往右位移元素，會覆蓋掉下一次迭代的元素，可考慮從結尾反向迭代

## Deletion
- 刪除元素的方法是以新元素覆蓋舊元素
- 建立變數length記錄刪除後實際的元素個數

刪除index=2的元素
```python
arr = [i for i in range(10)]
print(arr)

length = len(arr)
remove_idx = 2

for i in range(remove_idx, length - 1):
    arr[i] = arr[i+1]

length -= 1
print(arr[:length])
```