# 樹狀結構

## 定義
- 樹由一個以上的節點組成，每個節點可代表一些資料或指標組合成的紀錄
- 樹最上方的節點稱為root，其他節點都是root的子節點(子樹)
- 合法的樹的節點可連結，但不能形成沒有出口的循環

## 專有名詞
- 分支度(degree): 節點下有幾個子節點
- 階層(level): 樹的第幾層
- 高度(height): 樹的最大層數
- 樹葉(terminal node): 分支度為0的節點
- 父節點(parent): 一個節點的上一層節點
- 同代(generation): 同一層的節點
- 兄弟(siblings): 同個父節點的節點

## 二元樹Binary tree

對於一個n元樹來說，每個節點分支度不同，為了方便都要留長度為n的空間儲存鏈結，若有m個節點，則需m*n個空間。當為二元樹時，鏈結的浪費率最低，因此我們最常使用二元樹。

### 二元樹定義
- 二元樹可為空集合(樹則不行)
- 二元樹的節點分支度<=2，節點資料結構為llink, data, rlink
- 二元樹的子節點有次序關係(從左到右，從上到下)
- k層的二元樹節點最多有$\sum^k_{i=1}2^{i-1} = 2^k-1$


### 特殊二元樹
- fully binary tree: 節點數為$2^k-1$，其中k為level數
- complete binary tree: 節點數不滿$2^k-1$，但節點編號如同fully，從左到右，從上到下
- skewed binary tree: 完全沒有左或右節點
- stricky binary tree: 除了樹葉外，每個節點都有左右子樹

### 二元樹儲存方法

二元搜尋樹: 以array儲存樹結構，其中索引對應到樹節點的編號(從左到右，從上到下)，左子樹的值需小於父節點，索引是父節點索引x2，右子樹的值則需大於父節點，索引是父節點索引x2+1，不允許資料有重複值。

建立二元搜尋樹
```python
data = [0, 6, 3, 5, 7, 6, 8, 9, 2]
length = len(data)
btree = [0] * 16  # 怎麼知道長度16?

def create_btree(data, length, btree):
    for i in range(1, length):  # skip root
        idx = 1

        if data[i] > btree[idx]:
            idx = idx*2+1
        else:
            idx = idx*2
        btree[idx] = data[i]
    
    return btree

```


## 參考
