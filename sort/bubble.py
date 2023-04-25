#Bubble Sort

# 迭代檢查兩個相鄰數字，若前者比較大則交換位置
# 若陣列長度為n，則檢查次數為(n-1) + (n-2) + ... + 1 = n(n-1)/2
# 時間複雜度複平均O(n^2)
data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]

def bubble_sort(data):
    n = len(data)

    while n > 1:
        n -= 1
        for i in range(n):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
    
    return data

print(bubble_sort(data))