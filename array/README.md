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

## 常見的坑

*生成二維陣列*
請勿使用`[[0]*n]*m`複製陣列，這m個陣列是互相聯動。
請用[[0]*n for _ in range(m)]

*複製多種型別元素或多維度的陣列*
```python
import copy
copy.deepcopy(a)
```

*計算元素個數*
```python
num = [1, 2, 2, 3]
num.count(2)
```

*內建排序*
```python
num.sort()  # inplace
sorted(num)  # return new one
```

*用list實作queue*\
沒有效率，因為取出第一個元素時會移動後面的元素，請用deque