## 클래스와 함수 선언 부분 ##
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g): 
    global storeAry 
    
    print('', end='')
    for v in range(g.SIZE):
        print(storeAry[v], end='\t')   
    print()

    for row in range(g.SIZE):
        print(storeAry[row], end='\t\t')    
        for col in range(g.SIZE):
            print(f'{g.graph[row][col]:>4d}', end='\t\t')
        print()
    
    print()

## 전역 변수 선언 부분 ##
G1 = None
storeAry = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['blue25', 90], ['Emart24', 40]]
GS25, CU, Seven11, blue25, Emart24 = 0, 1, 2, 3, 4

## 메인 코드 부분 ##
SIZE = 5
G = Graph(SIZE)
G.graph[GS25][CU] = 1; G.graph[GS25][Seven11] = 1;
G.graph[CU][GS25] = 1; G.graph[CU][Seven11] = 1; G.graph[CU][blue25] = 1;
G.graph[Seven11][GS25] = 1; G.graph[Seven11][CU] = 1; G.graph[Seven11][blue25] = 1;
G.graph[blue25][Seven11] = 1; G.graph[blue25][CU] = 1; G.graph[blue25][Emart24] = 1;
G.graph[Emart24][blue25] = 1;

print('## 편의점 그래프 ## -> ', end=' ')
printGraph(G)

stack = []                  # 방문한 편의점
visitedAry = []

current = 0          # 시작 편의점
maxStore = current          # 최대개수 편의점 번호(GS25)
maxCount = storeAry[current][1]     # 편의점에 있는 허니버터 숫자
stack.append(current)
visitedAry.append(current)

while(len(stack) !=0):
    next = None
    for vertex in range(SIZE):
        if G.graph[current][vertex] == 1:
            if vertex in visitedAry:
                pass
            else:
                next = vertex
                break

    if next != None:
        current = next
        stack.append(current)
        visitedAry.append(current)
        if storeAry[current][1] > maxCount :
            maxCount = storeAry[current][1]
            maxStore = current
        else:                               # 방문할 다음 편의점이 없는 경우
            current = stack.pop()


print('허니버터칩 최대 보유 편의점(개수) =>', storeAry[maxStore][0], '(', storeAry[maxStore][1], ')')