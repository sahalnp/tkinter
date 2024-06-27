from tkinter import *

from tkinter import ttk


def dlt():
    item_box.delete(0, END)
    quantity_box.delete(0, END)
    price_box.delete(0, END)


def dlte_table():
    select = table.selection()[0]
    table.delete(select)


def calculate():
    qunty = float(quantity_box.get())
    price = float(price_box.get())
    total = qunty * price
    total_box.delete(0, END)
    total_box.insert(0, total)


def add_table():
    item = item_box.get()
    qunty = quantity_box.get()
    price = price_box.get()
    total = float(total_box.get())

    table.insert("", END, values=(item, qunty, price, total))
    dlt()


window = Tk()
window.geometry("600x600")
window.resizable(True, True)
window.title("Billing system")
heading = Label(
    window, text="billing system", font=("Arial", 20), bg="red", fg="yellow"
)
heading.pack(pady="20")  # pady=height
item_frame = Frame(window)
item_frame.pack()
for col in range(4):
    item_frame.columnconfigure(col, minsize=300)
item_label = Label(item_frame, text="item_name", font=("Arial", 20))
item_label.grid(row=0, column=0)
quantity_label = Label(item_frame, text="quantity", font=("Arial", 20))
quantity_label.grid(row=0, column=1)
price_label = Label(item_frame, text="price", font=("Arial", 20))
price_label.grid(row=0, column=2)
total_label = Label(item_frame, text="total", font=("Arial", 20))
total_label.grid(row=0, column=3)
item_box = Entry(item_frame, font=("Arial", 15), width=15)
item_box.grid(row=1, column=0)
quantity_box = Entry(item_frame, font=("Arial", 15), width=15)
quantity_box.grid(row=1, column=1)
price_box = Entry(item_frame, font=("Arial", 15), width=15)
price_box.grid(row=1, column=2)
total_box = Entry(item_frame, font=("Arial", 15), width=15)
total_box.grid(row=1, column=3)

calculate = Button(
    item_frame, text="calculate", font=("Arial", 20), fg="blue", command=calculate
)
calculate.grid(padx=20, row=2, column=1)

add = Button(item_frame, text="add", font=("italic", 20), fg="red", command=add_table)
add.grid(pady=20, row=2, column=2)

clear= Button(
    item_frame, text="clear", font=("Arial", 20), fg="blue", command=dlt
)
clear.grid(padx=20, row=2, column=3)

delete = Button(
    item_frame, text="delete table", font=("Arial", 20), fg="green", command=dlte_table
)
delete.grid(padx=20, row=2, column=4)

table = ttk.Treeview(
    item_frame,
    columns=("item", "qunty", "price", "total"),
    show="headings",
)
table.grid(row=3, column=0, columnspan=4,padx=10,pady=10)

table.heading("item", text="item")
table.heading("qunty", text="qunty")
table.heading("price", text="price")
table.heading("total", text="total")

window.mainloop()