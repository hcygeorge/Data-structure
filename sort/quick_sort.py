# 選擇一個pivot，然後用2 pointers從左右走訪數列
# 當左邊大於pivot且右邊小於pivot時交換數字，直到2 pointers相遇
# 交換pivot和2 pointers相遇點，此時pivot左邊的數字都小於pivot，右邊都大於pivot
# 對pivot左右兩邊的數列重複剛才的步驟(遞迴)
# 優點可以in place排序，空間複雜度O(1)

# 複雜度說明
# 因為每次走訪數列的複雜度為n，需要排序次數k，
# 每次排序n的長度減半，重複排序直到長度等於1，需要排序logn次(n/2^k = 1變成k = logn)
# 每次排序都會走過平均長度為n/2的數列
# 因此時間複雜度為(n/2)xlogn = O(nlogn)
# 若pivot選得不好導致兩個partition大小為1, n-1，則最差O(n^2)

def quick_sort(data: list, left: int, right: int):
    # end if length == 0
    if left >= right:
        return 
    
    # create pointer
    l, r = left, right

    # choose pivot
    pivot = data[left]

    # find data[l] > pivot and data[r] <= pivot
    while l < r:
        while data[l] <= pivot and l < r:
            l += 1
        while data[r] > pivot and l < r:
            r -= 1

        data[l], data[r] = data[r], data[l]

    # move pivot and update pivot
    data[left] = data[l]  # exchange l to pivot
    data[l] = pivot  # update pivot

    # partition
    quick_sort(data, left, l-1), quick_sort(data, l+1, right)


data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
quick_sort(data, 0, len(data)-1)
print(data)

