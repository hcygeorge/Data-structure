# 因為每次走訪數列的複雜度為n，需要遞迴次數k，
# 每次遞迴n的長度減半，直到長度等於1，需要遞迴logn次(n/2^k = 1變成k = logn)
# 因此時間複雜度平均與最佳為O(nlogn)
# 若pivot選得不好導致兩個partition大小為1, n-1，則最差O(n^2)
# 優點可以in place排序，空間複雜度O(1)

def quick_sort(data: list, left: int, right: int):
    # end if length == 0
    if left >= right:
        return 
    
    # create pointer
    l, r = left, right

    # choose pivot
    pivot = data[left]

    # exchange
    while l < r:
        while data[l] <= pivot and l < r:
            l += 1
        while data[r] > pivot and l < r:
            r -= 1

        data[l], data[r] = data[r], data[l]

    # rank pivot
    data[left] = data[l]
    data[l] = pivot

    # partition
    quick_sort(data, left, l-1), quick_sort(data, l+1, right)


data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
quick_sort(data, 0, len(data)-1)
print(data)

