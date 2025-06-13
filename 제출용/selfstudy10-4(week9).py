from tkinter import *
from tkinter import messagebox

# ## 함수 선언 부분 ##
def keyEvent(event):
    # Shift 키와 함께 눌린 경우 처리
    if event.state & 0x0001:  # Shift 키가 눌린 상태인지 확인
        arrow_keys = {
            37: "왼쪽 화살표",
            38: "위쪽 화살표",
            39: "오른쪽 화살표",
            40: "아래쪽 화살표"
        }
        if event.keycode in arrow_keys:
            messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + " + arrow_keys[event.keycode])
        else:
            messagebox.showinfo("키보드 이벤트", "Shift + 다른 키")
    else:
        messagebox.showinfo("키보드 이벤트", "눌린 키 : " + chr(event.keycode))

# ## 메인 코드 부분 ##
window = Tk()
window.bind("<Key>", keyEvent)
window.mainloop()
