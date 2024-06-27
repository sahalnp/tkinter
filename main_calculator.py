from tkinter import *


def click(event):
    current = display.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)
            display.delete(0, END)
            display.insert(0, result)
        except ZeroDivisionError:
            display.delete(0,END)
            display.insert(0,"cannot divide by zero")
        except:
            display.delete(0,END)
            display.insert(0,"0")
    elif text == "Ac":
        display.delete(0, END)
    elif text == "del":
        current = current[:-1]
        display.delete(0, END)
        display.insert(0, current)
    else:
        display.insert(END, text)
        

   # display.insert(END, text)


window = Tk()
window.geometry("600x300")
window.resizable(True, True)
window.title("calculator")
display = Entry(window, font=("arial", 20), justify="right")
display.pack(
    fill=X, padx=20, pady=20, ipady=10
)  # ullill ulla value size-ipady,fill=x paranna x coordinate
button_frame = Frame(window)
button_frame.pack()
button_label = [
    "7",
    "8",
    "9",
    "+",
    "4",
    "5",
    "6",
    "-",
    "3",
    "2",
    "1",
    "*",
    "Ac",
    "0",
    "del",
    "/",
    "=",
]
i = 0
for label in button_label:
    button = Button(button_frame, text=label, font=("Arial", 20), padx=20, pady=20)
    button.grid(row=i // 4, column=i % 4, padx=20, pady=20)
    i += 1 
    button.bind("<Button-1>", click)
window.mainloop()
