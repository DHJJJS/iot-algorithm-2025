# Test_481p.py
# 편의점에서 판매된 물건 목록과 개수세기

def binSearch(ary, fData):
    start = 0
    end = len(ary) - 1

    while (start <= end):
        mid = (start+end) // 2
        if fData == any[mid]:
            return mid
        elif fData > ary[mid]:
            start = mid + 1
        else :
            end = mid - 1

    return -1

## 전역 변수 선언 부분 ##
dataAry = ['바나나맛우유', '레쓰비캔커피', '츄파츕스', '도시락', '삼다수', '코카콜라', '삼각김밥']
sellAry = [random.choice(dataAry) for _ in range(20)]

## 메인 코드 부분 ##
print('#오늘 판매된 전체 물건(중복O, 정렬X) -->', sellAry)
sellAry.sort()
print('#오늘 판매된 전체 물건(중복O, 정렬O) -->', sellAry)
sellProduct = list(set(sellAry))
print('#오늘 판매된 물품 종류(중복x) -->', sellProduct)

countList = []
for product in sellProduct:
    count = 0
    pos = 0
    while (pos != -1):
        pos = binSearch(sellAry, product)
        if pos != -1:
            count += 1
            del (sellAry[pos])
    countList.append((product, count))

print()
print("결산 결과 ==>", countList)

# 순차 검색과 이진 검색의 성능 비교하기

import random

def seqSearch(ary, fData):
    global count
    pos = -1
    for i in range(len(ary)):
        count += 1
        if ary[i] == fData:
            pos = i
            break
    return pos

def binSearch(ary, fData):
    global count
    start = 0
    end = len(ary) - 1

    while (start <= end):
        count += 1
        mid = (start + end) // 2

        if fData == ary[mid]:
            return mid
        elif fData > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

dataAry, sortedAry = [], []
findData = 7878
count = 0

dataAry = [ random.randint(0, 999999) for _ in range(1000000)]
dataAry.insert(random.randint(0, 1000000), findData)
sortedAry = sorted(dataAry)

print('#비정렬 배열(100만개) -->', dataAry[0:5], '~~~', dataAry[-5:len(dataAry)])
print('#정렬 배열(100만개) -->', sortedAry[0:5], '~~~', sortedAry[-5:len(dataAry)])

count = 0
pos = seqSearch(dataAry,findData)
if pos !=-1:
    print('순차 검색(비정렬 데이터) -->', count, '회')

count = 0
pos = binSearch(sortedAry, findData)
if pos !=-1:
    print('이진 검색(정렬 데이터) -->', count, '회')