# TesT_147p.py

memory = []   
head, prev, curr = None, None, None 
dataArray = [["지민", "010-1111-1111"], ["정국", "010-2222-2222"], ["뷔", "010-3333-3333"], ["슈가", "010-4444-4444"], ["진", "010-5555-5555"]]

class Node:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone
        self.__link = None

    def setLink(self, link):
        self.__link = link

    def getName(self):
        return self.__name

    def getPhone(self):
        return self.__phone

    def getLink(self):
        return self.__link

def insertNode(findData, insertName, insertPhone):
    global memory, head, prev, curr  

    node = Node(insertName,insertPhone)

    # 맨 처음에 데이터 삽입
    if head.getName() == findData:
        node.setLink(head)  
        head = node  
        return

    curr = head
    while curr.getLink() is not None:
        prev = curr
        curr = curr.getLink()
        if curr.getName() == findData:
            node.setLink(curr)
            prev.setLink(node)
            return
        
    curr.setLink(node)
    
def printNodes(start):
    curr = start
    if curr == None: return

    print(curr.getName(), curr.getPhone(), end='->')

    while curr.getLink() != None: # 현재링크의 다음링크가 있는 동안
        curr = curr.getLink() # 다음 노드를 가리킴
        if curr.getLink() == None: # 더이상 다음 노드가 없으니 화살표 필요없음
            print(curr.getName(), curr.getPhone(), end=' ')
        else:
            print(curr.getName(), curr.getPhone(), end='->')

    print() # 그냥 한줄 내려줌

if __name__ == '__main__': # 시작 모듈일 때

    node = Node(dataArray[0][0], dataArray[0][1])
    head = node
    memory.append(node)

    for name, phone in dataArray[1:]: # '정연' 부터 사용
        prev = node # 다현이 들어있는 노드를 prev 할당
        node = Node(name, phone)  # 0/정연, 1/쯔위, 2/사나, 3/지효
        prev.setLink(node)  # 이전 노드에 현재 노드를 연결
        memory.append(node)

    printNodes(head)