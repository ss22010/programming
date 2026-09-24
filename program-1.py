import tkinter as tk
from tkinter import *
from builtins import range
import customtkinter as ctk

ADDITIONS = {
    "sockets": [
        {"1g": 1}, 
        {"2g": 0}

    ],
    "bedrooms": [{"number of heat pumps": 0}],
    "network_pts": [{"number of network points": 2}]
}

button_refs = {}
selections = {}

TEXT = {
    "kitchen": [
        {"Option A": "Upgrades units and worktop"},
        {"Option B": "As A plus induction hob"},
        {"Option C": "As A plus Deluxe appliance pack"}
    ],

    "bathroom": {
        "upgrade": [
            "Tiles",
            "Spa Bath",
            "Shower",
            "Tapware" 
        ]    
    },

    "living room": [
        {"add": "TV point plus roof mounted aerial"},
        {"add": "TV point plus satellite dish"},
        {"add": "4.5 KW Heat pump"}
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

        selections[room] = ctk.StringVar(value="") 

        if room == "kitchen":
            for option_dict in upgrades:
                for key, value in option_dict.items():
                    option = ctk.CTkRadioButton(group, text=value, variable=selections[room], value=key)
                    option.pack(anchor="w", padx=20, pady=2)

        elif room == "bathroom":
            for key, values in upgrades.items():
                if key == "upgrade" and isinstance(values, list):
                    option = ctk.CTkCheckBox(group, text=key.capitalize(), variable=selections[room])
                    option.pack(anchor="w", padx=20, pady=2)

                    for sub_value in values:
                        sub_option = ctk.CTkLabel(group, text=sub_value)
                        sub_option.pack(anchor="w", padx=40, pady=2)
        elif room == "living room":
            for item in upgrades:
                if isinstance(item, dict) and "add" in item:
                    option = ctk.CTkCheckBox(group, text=item["add"], variable=selections[room])
                    option.pack(anchor="w", padx=20, pady=2)

def create_int_card(ADDITIONS):

    for key, values in ADDITIONS.items():
        group = ctk.CTkFrame(root)
        group.pack(padx=10, pady=10, fill="x")

        title = ctk.CTkLabel(group, text=key.upper(), font=("Times", 18, "bold"))
        title.pack(pady=10)

        for item in values:
            if isinstance(item, dict):
                for sub_key, sub_value in item.items():

                    key_label = ctk.CTkLabel(group, text=sub_key)
                    key_label.pack(side="left", padx=5)

                    value_label = ctk.CTkLabel(group, text=str(sub_value))
                    value_label.pack(side="left", padx=5)

                    plus_btn = ctk.CTkButton(group, text="+", command=lambda sk=sub_key, item=item, vlabel=value_label: plus_btn_action(sk, item, vlabel))
                    plus_btn.pack(side="left", padx=5)

                    minus_btn = ctk.CTkButton(group, text="-", command=lambda sk=sub_key, item=item, vlabel=value_label: minus_btn_action(sk, item, vlabel))
                    minus_btn.pack(side="left", padx=5)
                    

def plus_btn_action(sub_key, item, value_label):
    if sub_key not in item:
        return

    current_value = item[sub_key]
    new_value = current_value + 1

    for category, values in ADDITIONS.items():
        if item in values:

            total = sum(value for dictionary in values for value in dictionary.values())

            if category == "sockets":
                limit = 12

            elif category == "bedrooms":
                limit = 2

            elif category == "network_pts":
                limit = 8

            if total >= limit:
                item[sub_key] = current_value
                value_label.configure(text=f"{current_value} maximum limit reached")
            else:
                item[sub_key] = new_value
                value_label.configure(text=str(new_value))

            break

        

def minus_btn_action(sub_key, item, value_label):
    if sub_key not in item:
        return

    current_value = item[sub_key]
    new_value = current_value - 1

    for category, values in ADDITIONS.items():

        if item in values:

            total = sum(value for dictionary in values for value in dictionary.values())

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
                item[sub_key] = new_value
                value_label.configure(text=str(new_value))

            break

create_card()
create_int_card(ADDITIONS)
root.mainloop()
