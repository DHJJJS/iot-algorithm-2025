# Test_311p.py

import os

class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

memory = []
root = None
fnameAry = []

folderName = 'C:/Program Files/Common Files/'

# 폴더 내 파일명 가져오기
for dirName, subDirList, fnames in os.walk(folderName):
    for fname in fnames:
        fnameAry.append(fname)

# 루트 노드 생성
node = TreeNode()
node.data = fnameAry[0]
root = node
memory.append(node)

dupNameAry = []  # 중복된 파일 목록 저장

# 이진 탐색 트리(BST)에 파일 이름 저장
for name in fnameAry[1:]:
    node = TreeNode()
    node.data = name

    current = root
    while True:  # 트리를 탐색하며 삽입할 위치 찾기
        if name == current.data:
            dupNameAry.append(name)  # 중복된 파일 이름 저장
            break

        elif name < current.data:  # 왼쪽 서브트리로 이동
            if current.left is None:
                current.left = node  # 왼쪽 자식으로 추가
                memory.append(node)
                break
            current = current.left  # 왼쪽으로 이동

        else:  # 오른쪽 서브트리로 이동
            if current.right is None:
                current.right = node  # 오른쪽 자식으로 추가
                memory.append(node)
                break
            current = current.right  # 오른쪽으로 이동

# 중복 파일 목록 중복 제거 (중복 저장된 경우 방지)
dupNameAry = list(set(dupNameAry))

# 결과 출력
print(f'{folderName} 및 그 하위 디렉터리의 중복된 파일 목록 --> ')
print(dupNameAry)
