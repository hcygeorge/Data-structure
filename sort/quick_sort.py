

def quick_sort(data: list, left: int, right: int):
    # 結束條件
    if left >= right:
        return 
    
    # 建立pointer
    l, r = left, right

    # 決定基準點pivot
    pivot = data[left]

    while l < r:
        while data[l] <= pivot and l < r:
            l += 1
        while data[r] > pivot and l < r:
            r -= 1

        data[l], data[r] = data[r], data[l]  # 交換大小值

    # 移動pivot
    data[left] = data[l]
    data[l] = pivot

    quick_sort(data, left, l-1), quick_sort(data, l+1, right)  # 繼續排序pivot兩側的陣列


data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
quick_sort(data, 0, len(data)-1)
print(data)

