# 用陣列結構(python list)實作堆疊
class StackWithList():
    def __init__(self, maxstack=10):
        self.MAXSTACK = maxstack
        self.stack = [None] * self.MAXSTACK  # 宣告堆疊陣列
        self.top=-1  # 堆疊頂端索引，-1代表頂端沒資料

    def is_empty(self):
        if self.top==-1:
            return True
        else:
            return False

    # 定義資料如何存入
    def push(self, data):
        if self.top >= self.MAXSTACK-1:
            print('stack is full')
        else:
            self.top += 1
            self.stack[self.top] = data
            print('push:', data)

    # 定義資料如何取出
    def pop(self):
        if self.is_empty():
            print('stack is empty')
        else:
            print('pop:', self.stack[self.top])
            self.stack[self.top] = None
            self.top -= 1

if __name__ == "__main__":
    # 堆疊過程
    stack01 = StackWithList()
    while True:
        command = int(input("1=push data, 0=pop data, -1=end: "))
        if command == -1:
            break
        elif command == 1:
            data = int(input('input integer value: '))
            stack01.push(data)
        elif command == 0:
            stack01.pop()

    # 列印堆疊內容
    print(stack01.stack)
    
