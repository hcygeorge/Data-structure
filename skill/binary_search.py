# Binary Search
# applicability
# 在已經排序且內容不重複的資料中尋找特定數字的索引
# 或是沒排序的資料，在不先排序下的解法時間複雜度超過O(nlogn)，則可以先排再搜

# SOP
# 在排序的資料中搜尋，每次以資料的中位數將資料切半，反覆縮小搜尋上下界，直到中位數等於搜尋目標或上下界交叉為止。若找不到目標，則下界位置會是插入新資料的點。


# complexity
#令x為搜尋次數，數據量為n，則2^x=n，等式兩邊取log_2，得到搜尋次數為x=logn，因此時間複雜度為O(logn)

# relate topics
# - Search Insert Position
# - First Bad Version

# blind spot:
# 用mid切開數列後對子數列遞迴，結果找到的是子數列的索引而非原始數列的，這個作法(quick select)只適用於找數字本身而非索引
# 因為可能無解，所以while的條件應該是lower <= upper，而非nums[mid] != target
# 注意while lower <= upper有等號，會導致最後一次lower被加1，剛好是無解時插入新值的位置

# attempt count: 3

# sample code
nums = [-1,0,3,5,9,12]  # already sorted and non-repeated array
target = 9

def binarySearch(nums, target):
    # find median index
    upper, lower = len(nums)-1, 0
    
    while lower <= upper:
        mid = (upper + lower) // 2
        
        if nums[mid] < target:
            lower = mid + 1
        elif nums[mid] > target:
            upper = mid - 1
        else:
            print(mid)
            return mid
    
    return lower

binarySearch(nums, target)
