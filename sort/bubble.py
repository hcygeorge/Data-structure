#Bubble Sort
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