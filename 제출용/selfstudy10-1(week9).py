from tkinter import *

window = Tk()
window.title("냥이들 ^^")  # 창 제목 설정

# 첫 번째 이미지
photo1 = PhotoImage(file="gif/cat1.gif")
label1 = Label(window, image=photo1)
label1.pack(side=LEFT)

# 두 번째 이미지
photo2 = PhotoImage(file="gif/cat2.gif")
label2 = Label(window, image=photo2)
label2.pack(side=LEFT)

window.mainloop()
