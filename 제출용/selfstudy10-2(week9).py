from tkinter import *
import random  # 이미지 순서를 섞기 위해 random 모듈 추가

## 전역 변수 선언 부분 ##
btnList = [None] * 9
fnameList = ["froyo.gif", "gingerbread.gif", "honeycomb.gif", "icecream.gif",
             "jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif", "nougat.gif"]

random.shuffle(fnameList)  # 이미지 파일 리스트를 실행할 때마다 무작위로 섞음

photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

## 메인 코드 부분 ##
window = Tk()
window.geometry("210x210")

for i in range(0, 9):
    photoList[i] = PhotoImage(file="gif/" + fnameList[i])
    btnList[i] = Button(window, image=photoList[i])

for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()
