# 可分成divide和merge兩部分
# 先以遞迴將數列從中間切成兩塊，直到數列長度=1，無法再切為止，回傳數列
# 從左邊開始迭代兩個數列，將最小的值插入到新數列，直到其中一個數列的值用完
# 剩下的數列全部插入到新數列的最右邊，回傳新數列
# 時間複雜度固定O(nlogn)，空間複雜度O(n)

# 適用於不要求in place(空間複雜度O(1))的排序
# 若要in place則複雜度會提高，建議用quick sort
# 有個例外是若排序linked list，可以透過改next保持空間複雜度O(1)

def merge_sort(data):
    # 當數列長度=1，回傳數列
    if len(data) < 2:
        return data
    mid = len(data) // 2
    l = data[:mid]
    r = data[mid:]
    
    # 遞迴將數列切成兩半
    return merge(merge_sort(l), merge_sort(r))

def merge(l, r):
    result = []
    # 兩個數列都有值就繼續比較大小，將較小的值插入新數列
    while len(l) > 0 and len(r) > 0:
        if l[0] <= r[0]:
            result.append(l.pop(0))
        else:
            result.append(r.pop(0))
    
    # 將剩下的數列插入右邊
    result += l or r
    
    return result

if __name__ == '__main__':
    data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
    merged = merge_sort(data)
    print(merged)