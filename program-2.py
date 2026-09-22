import tkinter as tk
from builtins import range
import customtkinter as ctk

class Layout():
    def __init__(self, root):
        self.root = root

        self.root.title("Waimak Builders Co")
        self.root.geometry("1200x700")
        self.root.configure(bg="white")

        self.create_layout()

    def create_layout(self):

        container = tk.Frame(self.root, bg="white")
        container.pack(expand=True, fill="both", padx=30, pady=30)

        for column in range(4):
            container.columnconfigure(column, weight=1)

        for row in range(2):
            container.rowconfigure(row, weight=1)

        for row in range(2):
            container.rowconfigure(row, weight=1)

        for row in range(2):
            for column in range(4):

                card = self.create_card(container)

                card.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

    def create_card(self, parent):

        card = ctk.CTkFrame(parent, fg_color="pink", corner_radius=18)

        image = ctk.CTkFrame(card, fg_color="blue")
        image.pack(fill="both", expand="True", padx=12, pady=12)
        image.configure(height=130)
        image.pack_propagate(False)

        bottom = ctk.CTkFrame(card, fg_color="purple")
        bottom.pack(fill="both", expand="True", padx=12, pady=12)

        text = ctk.CTkLabel(bottom, text=("lorem ipsum dolor sit amet consectetur adipiscing elit laboris quibusdam facilis duis dolor iusto esse commodo quibusdam eligendi sed iusto corrupti excepteur aute quis reprehenderit blanditiis cupiditate repellendus"), fg_color="yellow", text_color="black", justify="left", anchor="nw", wraplength=200)
        text.pack(side="left", fill="both", expand=True)

        buttons = ctk.CTkFrame(bottom, fg_color="orange")
        buttons.pack(side="right", padx=8)

        button_1 = ctk.CTkButton(buttons, text="", width=32, height=32, fg_color="red", corner_radius=16)
        button_1.pack(pady=4)

        button_2 = ctk.CTkButton(buttons, text="", width=32, height=32, fg_color="green", corner_radius=16)
        button_2.pack(pady=4)

        return card
    


root = tk.Tk()
Layout(root)

root.mainloop()

            
