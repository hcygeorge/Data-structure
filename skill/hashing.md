# Hashing

##
hash table是由key-value pairs組成的資料結構，其中hash function用於計算key與value的對應位置，使用hash function搜尋元素的時間複雜度為O(1)，搜尋時不同的key對應到相同位置的情況稱為碰撞(collision)，解決碰撞問題是設計hash function的重要課題。

## Python中內建的hash table:
- dict
- set

可將set看成value=Null的dict
