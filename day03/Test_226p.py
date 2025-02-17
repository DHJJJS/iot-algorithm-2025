# Test_226p.py

SIZE = 5
stack = [None, None, None, None, None]
top = -1

# 1번 삽입 탑관련 코드
def isStackFull(): # 스택이 꽉 찻는지 확인하는 함수
    global SIZE, stack, top
    if (top == SIZE - 1): # Full
        return True
    else:
        return False
    
def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False
def push(data): # 스택에 데이터 추가
    global SIZE, stack, top
    if isStackFull(): # isStackFull() == True와 동일
        print('Stack is full')
        stack[top] = data
        data = stack[top]
        stack[top] = None
        return
def pop(): 
    if isStackEmpty():
        print('Stack is empty.')
    else:
        global stack, top
        data = stack[top]
        stack[top] = None
        top -= 1
        return data