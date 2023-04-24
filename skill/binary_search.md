# Binary Search

## 方法
在排序的資料中搜尋，每次以資料的中位數將資料切半，反覆縮小搜尋上下界，直到中位數等於搜尋目標或上下界交叉為止。若找不到目標，則下界位置會是插入新資料的點。

## 適用範圍
- 已排序的資料，或是不排序的解法時間複雜度超過O(nlogn)
- 資料沒有重複(有重複則無法確定找的哪一筆資料)

## 時間複雜度
令$x$為搜尋次數，數據量為$n$，則$2^x=n$，等式兩邊取$log_2$，得到搜尋次數為$x=logn$，因此時間複雜度為O(logn)

## 相關題目
- Search Insert Position
- First Bad Version

## 作法
```python
# 定義上下界
lower = 1
upper = n
# 使用中位數檢查數據
mid = (lower + upper) // 2  # 整除
# 執行條件:只要lower<=upper，代表還沒找到唯一答案
# 注意有等號，會導致最後一次lower被加1，剛號是插入新值的位置
while lower <= upper:
    if isLarger(mid):
        lower = (mid+1)
    else:
        if isAnswer(mid):
            return mid
        else:
            upper = (mid-1)

    return None  # 答案不存在

```

## 參考資料
https://hiskio.com/courses/319/lectures/15379