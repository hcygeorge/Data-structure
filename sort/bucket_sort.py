# 將資料先分桶再排序
# 是需要額外空間的方法
# 因為是分配排序不是比較排序，所以不受O(nlogn)限制
# 平均複雜度是O(n+k)，k是桶子數量
# 如果數字集中在同個桶子，則排序越慢O(n^2)，反之若數字是均勻分配，則排序只要O(n)

# 適用範圍:
# 數字範圍相對小
# 有足夠的記憶體空間

def bucket_sort(data):
    # 以陣列範圍決定桶子數量並建立桶子
    max_x , min_x = max(data), min(data)
    shift = abs(min_x) + 10
    num_bucket = (max_x + shift) // 10 + 1  # 將數字變成非負整數再建立桶子
    bucket = [[] for _ in range(num_bucket)]
    # 走訪陣列並將數字並加入桶子
    for d in data:
        # 考慮再數字變成非負整數會分配到哪個桶子，但放入桶子的是原本的數字
        bucket[(d + shift) // 10].append(d)

    # 排序桶子內的數字，然後合併桶子
    res = []
    for b in bucket:
        if len(b) != 0:
            res += sorted(b)  # 這裡可使用任何比較排序法

    return res  # 因為放入桶子的是原始數字，所以不用復原

if __name__ == '__main__':
    data = [29, 25, 3, 49, 9, -201, 37, 21, 43, -83]
    sort_data = bucket_sort(data)
    print(sort_data)