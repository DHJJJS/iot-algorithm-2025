# fractal01

from tkinter import *

root = Tk()
# 윈도우창을 다 덮음 -> 그림을 그린다
canvas = Canvas(root, width=1000, height=1000, bg='white')
canvas.pack()
# 캔버스 생성 이후

cx = 1000 // 2
cy = 1000 // 2
r = 400

canvas.create_oval(cx-r, cy-r, cx+r, cy+r, width=2, outline='red')

root.mainloop()