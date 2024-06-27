from tkinter import *
window = Tk()
window.title("main heading")
window.geometry("300x300")
window.resizable(
    True, True
)  # to neettan thadi koottan first true=width,second truth=height
s = Entry(window)  # box ill ezhuthaan
s.pack()

def main():
    name=s.get()#entryill ulla value namill string aayi berum
    label2=Label(window,text="hello"+name)
    label2.pack()
    print("button clicked")
label=Label(window,text="sahal")
button = Button(window, text="click",command=main, width=20, fg="green",font=("impact ",20, "underline"))
button.pack(pady=16) # used combine button and windows, grid use chyymbo button pack use chyyoola
window.mainloop()
#for password  in entry show="*"
 