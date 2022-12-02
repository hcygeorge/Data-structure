# Hash Table

## 定義
Hash Table是由key-value pairs組成的資料結構，背後有hash function用於計算key對應的value，Hash Table的優點是插入、刪除、搜尋或修改元素的時間複雜度為O(1)。\
搜尋時不同的key對應到相同位置的情況稱為碰撞(collision)，解決碰撞問題是設計hash function的重要課題。

## Python中實作的hash table:
- Dictionary
- Set

(Java中為HashMap)

可將set看成不儲存value的dictionary

## 應用範圍
Hash Table常用於解決檢查重複資料或是計算重複次數的問題，例如:
- Check If N and Its Double Exist
- Contains Duplicate
- Two Sum
- Valid Anagram

Hash Table的資料無順序性，通常不能處理需要排序的問題。