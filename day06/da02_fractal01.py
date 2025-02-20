# fractal01

from tkinter import *

# 전역변수
count = 0
wsize = 1000
radius = 400

# 프랙탈 원그리기 재귀함수 선언
def drawCircle(x, y, r):
    global count
    count += 1
    canvas.create_oval(x-r, y-r, x+r, y+r)
    canvas.create_text(x, y-r, text=str(count), font=('', 30))

    if r >= radius/2: # 아직 매개변수로 받는 반지름이 기본사이즈보다 크면
        drawCircle(x-r//2, y, r//2) # 중심의 왼쪽을 계속 그려감
        drawCircle(x+r//2, y, r//2) # 중심의 오른쪽을 계속 그림

window = Tk()
window.title("원 모양의 프랙탈")
canvas = Canvas(window, height=wsize, width=wsize, bg='white')

drawCircle(wsize//2, wsize//2, radius)

canvas.pack()
window.mainloop()