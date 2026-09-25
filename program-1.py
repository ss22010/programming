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
selections = []

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

root = ctk.CTk()
root.geometry("1200x1200")
root.configure(bg="white")

def create_card():
    

    for room, upgrades in TEXT.items():
        

        group = ctk.CTkFrame(root)
        group.pack(padx=10, pady=10, fill="x")

        title = ctk.CTkLabel(group, text=room.upper(), font=("Times", 18, "bold"))
        title.pack(pady=10)
        
        if room == "kitchen":
            var = tk.StringVar()
            var.set(upgrades[0])
        
            def radio_ticked():
                print(var.get())
            
            for item in upgrades:
                option = ctk.CTkRadioButton(group, text=item["text"], variable=var, value=item["option"], command=radio_ticked)
                option.pack(anchor="w", padx=20, pady=2)

        else:
            for item in upgrades:
                checkbox_var = ctk.BooleanVar(value=False)
                option = ctk.CTkCheckBox(group, text=item["text"], command=lambda item=item, var=checkbox_var: ticked(item, var))
                option.pack(anchor="w", padx=20, pady=2)



def ticked(item, var=None):
    if var is None:
        for selected in selections[:]:
            if selected in TEXT["kitchen"]:
                selections.remove(selected)

        selections.append(item)

    else:
        if var.get():
            if item not in selections:
                selections.append(item)
        else:
            if item in selections:
                selections.remove(item)

    print(selections)

def create_int_card(ADDITIONS):

    for key, values in ADDITIONS.items():
        group = ctk.CTkFrame(root)
        group.pack(padx=10, pady=10, fill="x")

        title = ctk.CTkLabel(
            group,
            text=key.upper(),
            font=("Times", 18, "bold")
        )
        title.pack(pady=10)

        for item in values:

            sub_key = item["name"]
            sub_value = item["value"]
            price = item["price"]

            key_label = ctk.CTkLabel(group, text=f"{sub_key} (${price})")
            key_label.pack(side="left", padx=5)

            value_label = ctk.CTkLabel(group, text=str(sub_value))
            value_label.pack(side="left", padx=5)

            plus_btn = ctk.CTkButton(group, text="+", command=lambda item=item, vlabel=value_label: plus_btn_action(item, vlabel))
            plus_btn.pack(side="left", padx=5)

            minus_btn = ctk.CTkButton(group, text="-", command=lambda item=item, vlabel=value_label: minus_btn_action(item, vlabel))
            minus_btn.pack(side="left", padx=5)
                        
def plus_btn_action(item, value_label):

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
            break   

def minus_btn_action(item, value_label):

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
            break

def total_price():
    pass

create_card()
create_int_card(ADDITIONS)
root.mainloop()
