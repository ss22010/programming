import tkinter as tk
from tkinter import ttk

# initial layout for the grids inside the grid 
class Layout():
    def __init__(self, card, root, bottom, button, row, col):
        self.card = tk.Frame(root, bg="white", bd=1, relief="solid")
        self.card.grid(row=row, column=col, padx=15, pady=15)
        self.image = tk.Frame(card, bg="blue", width=200, height=120).pack().pack_propagate(False)
        self.bottom = tk.Frame(card, bg="blue", width=200, height=100).pack().pack_propagate(False)
        self.text = tk.Label(bottom, text="Lorem ipsium", bg="white", justify="left").pack(side="left", padx=10)
        self.button = tk.Frame(bottom, bg="white").pack(side="right", padx=5)
        self.button = tk.Button(button, text="+", width=2).pack(pady=3)

root = tk.Tk()

for row in range(2):
    for col in range(4):
        
        Layout()


root.mainloop()