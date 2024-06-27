from tkinter import *
from tkinter import ttk

def dlt():
    item_box.delete(0, END)
    quantity_box.delete(0, END)
    price_box.delete(0, END)
    total_box.delete(0, END)

def dlte():
    selected_item = table.selection()
    if selected_item:
        table.delete(selected_item[0])

def calculate():
    try:
        qunty = float(quantity_box.get())
        price = float(price_box.get())
        total = qunty * price
        total_box.delete(0, END)
        total_box.insert(0, total)
    except ValueError:
        total_box.delete(0, END)
        total_box.insert(0, "Error")

def add_table():
    item = item_box.get()
    qunty = quantity_box.get()
    price = price_box.get()
    total = float(total_box.get())

    if item and qunty and price:
        table.insert("", END, values=(item, qunty, price, total))
        dlt()  # Clear entry fields after adding

window = Tk()
window.geometry("600x600")
window.resizable(True, True)
window.title("Billing system")

heading = Label(
    window, text="Billing System", font=("Arial", 20), bg="red", fg="yellow"
)
heading.pack(pady="20")  # pady=height

item_frame = Frame(window)
item_frame.pack()

# Labels
labels = ["Item Name", "Quantity", "Price", "Total"]
for col, label_text in enumerate(labels):
    label = Label(item_frame, text=label_text, font=("Arial", 20))
    label.grid(row=0, column=col, padx=10, pady=5)

# Entry boxes
item_box = Entry(item_frame, font=("Arial", 15), width=15)
item_box.grid(row=1, column=0, padx=10)
quantity_box = Entry(item_frame, font=("Arial", 15), width=15)
quantity_box.grid(row=1, column=1, padx=10)
price_box = Entry(item_frame, font=("Arial", 15), width=15)
price_box.grid(row=1, column=2, padx=10)
total_box = Entry(item_frame, font=("Arial", 15), width=15)
total_box.grid(row=1, column=3, padx=10)

# Buttons
calculate_btn = Button(
    item_frame, text="Calculate", font=("Arial", 20), fg="blue", command=calculate
)
calculate_btn.grid(padx=20, row=2, column=1)

add_btn = Button(item_frame, text="Add", font=("Arial", 20), fg="red", command=add_table)
add_btn.grid(pady=20, row=2, column=2)

delete_btn = Button(
    item_frame, text="Clear", font=("Arial", 20), fg="blue", command=dlt
)
delete_btn.grid(padx=20, row=2, column=3)

delete_table_btn = Button(
    item_frame, text="Delete from Table", font=("Arial", 20), fg="green", command=dlte
)
delete_table_btn.grid(padx=20, row=2, column=0)

table = ttk.Treeview(
    item_frame,
    columns=("item", "qty", "price", "total"),
    show="headings",
)
table.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

table.heading("item", text="Item")
table.heading("qty", text="Quantity")
table.heading("price", text="Price")
table.heading("total", text="Total")

window.mainloop()
