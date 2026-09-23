import tkinter as tk
from tkinter import *
from builtins import range
import customtkinter as ctk


class Layout():
    def __init__(self, root):
        self.root = root

        self.root.title("Waimak Builders Co")
        self.root.geometry("1200x1200")
        self.root.configure(bg="white")

        self.create_layout()


    def create_layout(self):

        banner = tk.Frame(self.root, bg="black", height=200)
        banner.pack(fill="x", padx=30, pady=(0,10))
        banner.pack_propagate(False)

        title = tk.Label(banner, text="Waimak Builders Co", bg="black", fg="white", font=("Arial", 24, "bold"))
        title.pack(expand=True)

        description = ctk.CTkLabel(banner, text="The Waimak Build Co is a local company that supply a range of flatpack houses to the building trade and to retail customers. These are supplied as a kit that the customer then assembles themselves. The kit offers limited scope for customisation, to keep the cost as low as possible.", text_color="white", justify="center", wraplength=1000)
        description.pack(pady=(0,10), padx=10)

        add_account = ctk.CTkButton(banner, text="Account")
        add_account.pack()

        cart = ctk.CTkButton(banner, text="Cart")
        cart.pack()

        default_bar = tk.Frame(self.root, bg="purple")
        default_bar.pack(fill="x", padx=30, pady=(0,10))
        default_bar.pack_propagate(False)

        d_settings = ctk.CTkLabel(default_bar, text="The basic kit costs $75,000 inclusive of taxes and delivery, and measures 8m x 8m. It includes a basic but functional bathroom, 2 bedrooms, a ‘standard’ fitted kitchen with space for a washing machine or dishwasher and a living room. All windows are double glazed, walls, floor and loft insulated to NZ standards. All rooms come with 1 double electrical socket as standard.", text_color="white", justify="left", wraplength=500)
        d_settings.grid(row=0, column=0, pady=30, padx=30)

        d_img = ctk.CTkFrame(default_bar, fg_color="orange", height=100, width=550, corner_radius=18)
        d_img.grid(row=0, column=1, pady=10, padx=10)

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
        image.pack(fill="both", expand="True", padx=12, pady=(12,0))
        image.configure(height=130)
        image.pack_propagate(False)

        bottom = ctk.CTkFrame(card, fg_color="purple")
        bottom.pack(fill="both", expand="True", padx=12, pady=12)

        text = ctk.CTkLabel(bottom, text=("lorem ipsum dolor sit amet consectetur adipiscing elit laboris quibusdam facilis duis dolor iusto esse commodo quibusdam eligendi sed iusto corrupti excepteur aute quis reprehenderit blanditiis cupiditate repellendus"), fg_color="yellow", text_color="black", justify="left", anchor="nw", pady=10, padx=10, wraplength=190)
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

            
