import tkinter as tk
from tkinter import *
from builtins import range
import customtkinter as ctk

ADDITIONS = {
    "sockets": [
        {
            "name": "1g", 
            "value": 1, 
            "price": 40
        },
        {
            "name": "2g", 
            "value": 0, 
            "price": 50
        }
    ],
    "bedrooms": [
        {
            "name": "number of heat pumps", 
            "value": 0, 
            "price": 1800
        }
    ],
    "network_pts": [
        {
            "name": "number of network points", 
            "value": 2, 
            "price": 50
        }
    ]
}

button_refs = []
selections = {}

TEXT = {
    "kitchen": [
        {
            "option": "Default",
            "text": "Default",
            "price": 0
        },
        {
            "option": "Option A",
            "text": "Upgrades units and worktop",
            "price": 2000
        },
        {
            "option": "Option B",
            "text": "As A plus induction hob",
            "price": 3500
        },
        {
            "option": "Option C",
            "text": "As A plus Deluxe appliance pack",
            "price": 6000
        }
    ],
    "bathroom": [
        {
            "option": "upgrade",
            "text": "Tiles, Spa Bath, Shower, Tapware",
            "price": 2500
        }
    ],
    "living room": [
        {
            "option": "add",
            "text": "TV point plus roof mounted aerial",
            "price": 250
        },
        {
            "option": "add",
            "text": "TV point plus satellite dish",
            "price": 250
        },
        {
            "option": "add",
            "text": "4.5 KW Heat pump",
            "price": 2500
        }
    ]
}


class Layout():
    def __init__(self, root):
        self.root = root

        self.root.title("Waimak Builders Co")
        self.root.geometry("1200x1000")
        self.root.configure(bg="white")

        self.scroll_frame = ctk.CTkScrollableFrame(self.root)
        self.scroll_frame.pack(expand=True, fill="both", padx=30, pady=10)

        self.card_index = 0

        self.create_card()
        self.create_int_card(ADDITIONS)

    def add_card(self, card):

        row = self.card_index // 2
        column = self.card_index % 2

        card.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

        self.card_index += 1

    def checkbox_ticked(self, item, var):
        key = (item["option"], item["text"])
        if var.get():
            selections[key] = item
        else:
            selections.pop(key, None)
        self.total_price()

    def create_card(self):
        banner = tk.Frame(self.scroll_frame, bg="black", height=200)
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

        default_bar = tk.Frame(self.scroll_frame, bg="purple")
        default_bar.pack(fill="x", padx=30, pady=(0,10))
        default_bar.pack_propagate(False)

        d_settings = ctk.CTkLabel(default_bar, text="The basic kit costs $75,000 inclusive of taxes and delivery, and measures 8m x 8m. It includes a basic but functional bathroom, 2 bedrooms, a ‘standard’ fitted kitchen with space for a washing machine or dishwasher and a living room. All windows are double glazed, walls, floor and loft insulated to NZ standards. All rooms come with 1 double electrical socket as standard.", text_color="white", justify="left", wraplength=500)
        d_settings.grid(row=0, column=0, pady=30, padx=30)

        d_img = ctk.CTkFrame(default_bar, fg_color="orange", height=100, width=400, corner_radius=18)
        d_img.grid(row=0, column=1, pady=10, padx=10)

        self.container = tk.Frame(self.scroll_frame, bg="white")
        self.container.pack(expand=True, fill="both", padx=30, pady=30)

        self.container.columnconfigure(0, weight=1)
        self.container.columnconfigure(1, weight=1)

        card_index = 0

        for room, upgrades in TEXT.items():
            row = card_index // 2
            column = card_index % 2

            card, bottom = self.create_layout(self.container, card_type=room)
            card.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

            self.add_card(card)

            card_index +=1

            if room == "kitchen":
                var = tk.StringVar(value=upgrades[0]["option"])
            
                def radio_ticked(var=var, upgrades=upgrades):
                    selected = next(item for item in upgrades if item["option"] == var.get())
                    selections["kitchen"] = selected
                    self.total_price()


                selections["kitchen"] = upgrades[0]
                
                for item in upgrades:
                    option = ctk.CTkRadioButton(bottom, text=item["text"], variable=var, value=item["option"], command=radio_ticked)
                    option.pack(anchor="w", padx=20, pady=2)

            else:
                for item in upgrades:
                    var = tk.BooleanVar(value=False)
                    option = ctk.CTkCheckBox(bottom, text=item["text"], variable=var, command=lambda item=item, var=var: self.checkbox_ticked(item, var))
                    option.pack(anchor="w", padx=20, pady=2)

    def create_layout(self, container, card_type):

        card = ctk.CTkFrame(container, fg_color="pink", corner_radius=18)

        image = ctk.CTkFrame(card, fg_color="blue", height=130)
        image.pack(fill="both", expand=True, padx=12, pady=(12, 0))
        image.pack_propagate(False)

        bottom = ctk.CTkFrame(card, fg_color="purple")
        bottom.pack(fill="both", expand=True, padx=12, pady=12)

        title = ctk.CTkLabel(bottom, text=card_type.upper(), font=("Times", 18, "bold"))
        title.pack(anchor="w", padx=15, pady=10)

        return card, bottom

    def create_int_card(self, ADDITIONS):
        card_index = 0
        for key, values in ADDITIONS.items():
            row = card_index // 2
            column = card_index % 2

            card, bottom = self.create_layout(self.container, card_type=key)
            card.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

            self.add_card(card)

            card_index +=1


            for item in values:

                controls = ctk.CTkFrame(bottom, fg_color="transparent")
                controls.pack(fill="x")

                sub_key = item["name"]
                sub_value = item["value"]
                price = item["price"]

                key_label = ctk.CTkLabel(controls, text=f"{sub_key} (${price})")
                key_label.pack(side="left", padx=5)

                value_label = ctk.CTkLabel(controls, text=str(sub_value))
                value_label.pack(side="left", padx=5)

                plus_btn = ctk.CTkButton(controls, text="+", height=10, width=10, corner_radius=50, command=lambda item=item, vlabel=value_label: self.plus_btn_action(item, vlabel))
                plus_btn.pack(side="left", padx=5, pady=5)

                minus_btn = ctk.CTkButton(controls, text="-", height=10, width=10, corner_radius=50, command=lambda item=item, vlabel=value_label: self.minus_btn_action(item, vlabel))
                minus_btn.pack(side="left", padx=5, pady=5)

    def plus_btn_action(self, item, value_label):

        current_value = item["value"]
        new_value = current_value + 1

        for category, values in ADDITIONS.items():

            if item in values:

                total = sum(dictionary["value"] for dictionary in values)

                if category == "sockets":
                    limit = 12

                elif category == "bedrooms":
                    limit = 2

                elif category == "network_pts":
                    limit = 8

                if total >= limit:
                    value_label.configure(text=f"{current_value} maximum limit reached")
                else:
                    item["value"] = new_value
                    value_label.configure(text=str(new_value))
                    key = (item["name"], item["price"])
                    selections[key] = item
                break   
        self.total_price()

    def minus_btn_action(self, item, value_label):

        current_value = item["value"]
        new_value = current_value - 1

        for category, values in ADDITIONS.items():

            if item in values:

                total = sum(dictionary["value"] for dictionary in values)

                if category == "sockets":
                    minimum = 1

                elif category == "bedrooms":
                    minimum = 0

                elif category == "network_pts":
                    minimum = 2

                if new_value < 0:
                    value_label.configure(text="0 minimum reached")
                elif total <= minimum:
                    value_label.configure(text=f"{current_value} minimum limit reached")

                else:
                    item["value"] = new_value
                    value_label.configure(text=str(new_value))
                    key = (item["name"], item["price"])
                    if new_value > minimum:
                        selections[key] = item
                    else:
                        selections.pop(key, None)
                        self.total_price()
                break
        self.total_price()

    def total_price(self):
        total = 75000

        for item in selections.values():
            if "option" in item:
                total += item["price"]
            else:
                total += item["value"] * item["price"]

        lbl.configure(text=f"Total price: ${total:,.2f}")

        return total




root = ctk.CTk()

lbl = ctk.CTkLabel(root, text="Total price: $75,000.00")
lbl.pack(side="bottom", pady=10)

Layout(root)


root.mainloop()
