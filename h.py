import tkinter as tk
from tkinter import *
import customtkinter as ctk

root = ctk.CTk()
root.geometry("300x250")
root.configure(fg_color="white")

menu_items = {"eggs": 7, "chips": 1, "beer": 2}
selected = {}

def calculate():
    bill = 0

    for item in menu_items:
        if selected[item].get():
            bill += menu_items[item]

    results.delete(1.0, END)
    results.insert(END, "Total cost - £" + str(bill))

for item in menu_items:
    is_selected = BooleanVar()
    button = Checkbutton(root, text=item, variable=is_selected)
    button.grid(sticky="w")
    selected[item] = is_selected

purchase_btn = Button(root, text="Calculate", command=calculate)
purchase_btn.grid()

results = Text(root, wrap=WORD)
results.grid(columnspan=2)

root.mainloop()