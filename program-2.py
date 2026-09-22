import tkinter as tk

# initial layout for the grids inside the grid 
class Layout():
    def __init__(self, contain, i, j, text="?"):
        self.text = tk.StringVar(contain, value=text)
        self.image = tk.PhotoImage(file="image.png")
        self.image.grid(row=i, column=j, sticky='nsew', pady=1, padx=1)
        self.label = tk.Label(contain, textvariable=self.text, image=self.image, compound="top")
        self.label.grid(row=i, column=j)
        self.row = i
        self.col = j

root = tk.Tk()

for outer_row in range(2):
    for outer_col in range(4):
        f = tk.Frame(root)
        f.grid(row=outer_row, column=outer_col, sticky='nsew', padx=20, pady=20)

        for inner_row in range(1):
            for inner_col in range(1):
                layout = Layout(f, inner_row, inner_col, text=f"Grid {outer_row},{outer_col} - Cell {inner_row},{inner_col}")


root.mainloop()
