import tkinter as tk
from tkinter import *
from builtins import range
import customtkinter as ctk

ADDITIONS = {
    "sockets": [
        {"1g": 1}, 
        {"2g": 0}

    ],
    "heat_pump": [{"number of heat pumps": 0}],
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

        if isinstance(upgrades, dict):
            for key, values in upgrades.items():
                option = ctk.CTkRadioButton(group, text=key, variable=selections[room], value=key)
                option.pack(anchor="w", padx=20, pady=5)
                if key == "upgrade" and isinstance(values, list):
                    for sub_value in values:
                        sub_option = ctk.CTkLabel(group, text=sub_value)
                        sub_option.pack(anchor="w", padx=40, pady=2)
        elif isinstance(upgrades, list):
            for item in upgrades:
                option = ctk.CTkRadioButton(group, text=item, variable=selections[room], value=item)
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

                    plus_btn = ctk.CTkButton(group, text="+", command=lambda k=key, sk=sub_key, item=item, vlabel=value_label: plus_btn_action(k, sk, item, vlabel))
                    plus_btn.pack(side="left", padx=5)

                    minus_btn = ctk.CTkButton(group, text="-", command=lambda k=key, sk=sub_key, item=item, vlabel=value_label: minus_btn_action(k, sk, item, vlabel))
                    minus_btn.pack(side="left", padx=5)
                    

def plus_btn_action(key, sub_key, item, value_label):
    if sub_key in item:

        if key == "sockets":
            bothg = sum(value for socket in ADDITIONS["sockets"] for value in socket.values())
            print(bothg)
            if bothg == 10:
                value_label.configure(text=f"{str(item[sub_key])} limit reached")
                

            elif 0 < bothg < 10:
                current_value = item[sub_key]
                new_value = current_value + 1
                item[sub_key] = new_value
                value_label.configure(text=f"{str(new_value)} {bothg}")


            elif bothg <= 0: 
                value_label.configure(text=f"{str(item[sub_key])} minimum reached")
            
         
        

def minus_btn_action(key, sub_key, item, value_label):
        if sub_key in item:
            current_value = item[sub_key]
            new_value = current_value - 1
            if new_value < 0:
                new_value = 0
            item[sub_key] = new_value

            if key == "sockets":
                bothg = sum(value for socket in ADDITIONS["sockets"] for value in socket.values())
                if bothg == 10:
                    value_label.configure(text=f"{str(new_value)} limit reached")
                elif 0 < bothg < 10:
                    value_label.configure(text=f"{str(new_value)} {bothg}")
                else: 
                    value_label.configure(text=f"{str(new_value)} minimum reached")
            

create_card()
create_int_card(ADDITIONS)
root.mainloop()
