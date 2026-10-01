import tkinter as tk
from tkinter import *
import customtkinter as ctk
import re
from PIL import Image

ADDITIONS = {
    "Sockets": [
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
    "Bedrooms": [
        {
            "name": "Number of heat pumps", 
            "value": 0, 
            "price": 1800
        }
    ],
    "Network Points": [
        {
            "name": "Number of network points", 
            "value": 2, 
            "price": 50
        }
    ]
}

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

button_refs = []
selections = {}
in_user = ""

purchaces = {

    "sarahs123": [
        {
            "Sockets": [
                {
                    "name": "1g",
                    "value": 4,
                    "price": 40
                },
                {
                    "name": "2g",
                    "value": 2,
                    "price": 50
                }
            ],

            "Bedrooms": [
                {
                    "name": "Number of heat pumps",
                    "value": 2,
                    "price": 1800
                }
            ],

            "Network Points": [
                {
                    "name": "Number of network points",
                    "value": 4,
                    "price": 50
                }
            ],

            "kitchen": [
                {
                    "option": "Option B",
                    "text": "As A plus induction hob",
                    "price": 3500
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
    ],


    "jamesw123": [

        {
            "Sockets": [
                {
                    "name": "1g",
                    "value": 6,
                    "price": 40
                },
                {
                    "name": "2g",
                    "value": 3,
                    "price": 50
                }
            ],

            "Bedrooms": [
                {
                    "name": "Number of heat pumps",
                    "value": 2,
                    "price": 1800
                }
            ],

            "Network Points": [
                {
                    "name": "Number of network points",
                    "value": 6,
                    "price": 50
                }
            ],

            "kitchen": [
                {
                    "option": "Option A",
                    "text": "Upgrades units and worktop",
                    "price": 2000
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
                }
            ]
        },


        {
            "Sockets": [
                {
                    "name": "1g",
                    "value": 3,
                    "price": 40
                },
                {
                    "name": "2g",
                    "value": 4,
                    "price": 50
                }
            ],

            "Bedrooms": [
                {
                    "name": "Number of heat pumps",
                    "value": 1,
                    "price": 1800
                }
            ],

            "Network Points": [
                {
                    "name": "Number of network points",
                    "value": 3,
                    "price": 50
                }
            ],

            "kitchen": [
                {
                    "option": "Option C",
                    "text": "As A plus Deluxe appliance pack",
                    "price": 6000
                }
            ],

            "bathroom": [],

            "living room": [
                {
                    "option": "add",
                    "text": "4.5 KW Heat pump",
                    "price": 2500
                }
            ]
        },


        {
            "Sockets": [
                {
                    "name": "1g",
                    "value": 8,
                    "price": 40
                },
                {
                    "name": "2g",
                    "value": 4,
                    "price": 50
                }
            ],

            "Bedrooms": [
                {
                    "name": "Number of heat pumps",
                    "value": 2,
                    "price": 1800
                }
            ],

            "Network Points": [
                {
                    "name": "Number of network points",
                    "value": 8,
                    "price": 50
                }
            ],

            "kitchen": [
                {
                    "option": "Default",
                    "text": "Default",
                    "price": 0
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
    ]
}

members = [
    {
        "name": {
            "first": "Sarah",
            "last": "Shaw"
        },
        "email": "123@gmail.com",
        "phone": "+64 0278293321",
        "username": "sarahs123",
        "password": "123!@#QWE"
    },
    {
        "name": {
            "first": "James",
            "last": "Wilson"
        },
        "email": "james@gmail.com",
        "phone": "+64 021234567",
        "username": "jamesw123",
        "password": "James123!@#",
        "company": "Wilson Builders"
    }
]

contain = [
    "Password required",
    "Must be greater than 5 characters long", 
    "Must contain one or more special charcaters",
    "Must contain one or more capital letters",
    "Must contain one or more numbers"
]

country_codes = [
    "American Samoa (+1 684)",
    "Argentina (+54)",
    "Australia (+61)",
    "Austria (+43)",
    "Bahamas (+1 242)",
    "Bangladesh (+880)",
    "Barbados (+1 246)",
    "Belgium (+32)",
    "Brazil (+55)",
    "Canada (+1)",
    "Chile (+56)",
    "China (+86)",
    "Colombia (+57)",
    "Cook Islands (+682)",
    "Costa Rica (+506)",
    "Czech Republic (+420)",
    "Denmark (+45)",
    "Egypt (+20)",
    "Fiji (+679)",
    "Finland (+358)",
    "France (+33)",
    "French Polynesia (+689)",
    "Germany (+49)",
    "Ghana (+233)",
    "Greece (+30)",
    "Guam (+1 671)",
    "Hong Kong (+852)",
    "Hungary (+36)",
    "Iceland (+354)",
    "India (+91)",
    "Indonesia (+62)",
    "Ireland (+353)",
    "Israel (+972)",
    "Italy (+39)",
    "Jamaica (+1 876)",
    "Japan (+81)",
    "Kenya (+254)",
    "Kiribati (+686)",
    "Malaysia (+60)",
    "Marshall Islands (+692)",
    "Mexico (+52)",
    "Micronesia (+691)",
    "Nauru (+674)",
    "Nepal (+977)",
    "Netherlands (+31)",
    "New Caledonia (+687)",
    "New Zealand (+64)",
    "Niue (+683)",
    "Northern Mariana Islands (+1 670)",
    "Norway (+47)",
    "Palau (+680)",
    "Pakistan (+92)",
    "Panama (+507)",
    "Papua New Guinea (+675)",
    "Peru (+51)",
    "Philippines (+63)",
    "Poland (+48)",
    "Portugal (+351)",
    "Russia (+7)",
    "Saudi Arabia (+966)",
    "Singapore (+65)",
    "Solomon Islands (+677)",
    "South Africa (+27)",
    "South Korea (+82)",
    "Spain (+34)",
    "Sri Lanka (+94)",
    "Sweden (+46)",
    "Switzerland (+41)",
    "Taiwan (+886)",
    "Thailand (+66)",
    "Tonga (+676)",
    "Trinidad and Tobago (+1 868)",
    "Turkey (+90)",
    "Tuvalu (+688)",
    "United Arab Emirates (+971)",
    "United Kingdom (+44)",
    "United States (+1)",
    "Vanuatu (+678)",
    "Vietnam (+84)"
]

class Layout():
    def __init__(self, root):
        self.root = root
        self.members = members

        self.root.title("Waimak Builders Co")
        self.root.geometry("1000x900")
        self.root.configure(fg_color="white")

        self.scroll_frame = ctk.CTkScrollableFrame(self.root, fg_color="white", border_color="#FFD700")
        self.scroll_frame.pack(expand=True, fill="both", padx=30, pady=10)

        self.card_index = 0

        self.signed_in = False

        self.private_frame = ctk.CTkFrame(self.scroll_frame, fg_color="transparent")
        self.private_frame.pack_forget()

        self.container = tk.Frame(self.private_frame, bg="white")
        self.container.pack(expand=True, fill="both", padx=30, pady=30)
        self.container.columnconfigure(0, weight=1)
        self.container.columnconfigure(1, weight=1)

        self.value_labels = []
        self.check_vars = []

        self.create_card()

        self.card_index = 0
        self.create_private_content()

        self.purchace_btn = ctk.CTkButton(self.private_frame, text="Purchace", command=self.purchace)
        self.purchace_btn.pack(pady=(0, 20))

        lbl.pack_forget()

    def purchace(self):
        purchace = {}

        for category, values in ADDITIONS.items():
            purchace[category] = [item.copy() for item in values]

        purchace["kitchen"] = [selections["kitchen"].copy()]

        for room in ["bathroom", "living room"]:
            purchace[room] = []

            for item in TEXT[room]:
                if item in selections.values():
                    purchace[room].append(item.copy())
            
        if self.current_user not in purchaces:
            purchaces[self.current_user] = []

        purchaces[self.current_user].append(purchace)

        ADDITIONS["Sockets"][0]["value"] = 1
        ADDITIONS["Sockets"][1]["value"] = 0
        ADDITIONS["Bedrooms"][0]["value"] = 0
        ADDITIONS["Network Points"][0]["value"] = 2

        selections.clear()

        for item, value_label in self.value_labels:
            value_label.configure(text=str(item["value"]))

        for var in self.check_vars:
            var.set(False)

        self.kitchen_var.set("Default")
        selections["kitchen"] = TEXT["kitchen"][0]

        msg_window = ctk.CTkToplevel(self.root)
        msg_window.title("Purchase")

        msg = ctk.CTkLabel(msg_window, text="Purchase successful!")
        msg.pack(expand=True)

        msg_window.after(3000, msg_window.destroy)


    def show_signed_in(self):
        self.signed_in = True

        self.auth_buttons.place_forget()
        self.user_buttons.place(relx=1.0, y=10, anchor="ne")

        self.private_frame.pack(expand=True, fill="both")
        lbl.pack(side="bottom", pady=10)
        self.total_price()

    def sign_out(self):
        self.signed_in = False
        self.user_buttons.place_forget()
        self.auth_buttons.place(relx=1.0, y=10, anchor="ne")
        self.private_frame.pack_forget()
        lbl.pack_forget()

    def open_cart(self):
        ReceiptsWindow(self.root, purchaces, username=self.current_user, layout=self)

    def open_account(self):
        username = getattr(self, "current_user", None)
        if username:
            AccountWindow(self.root, username, self.members, self)

    def add_card(self, card):

        row = self.card_index // 2
        column = self.card_index % 2

        card.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

        self.card_index += 1
    
    def create_private_content(self):
        card_index = 0

        self.kitchen_var = None

        for room, upgrades in TEXT.items():
            row = card_index // 2
            column = card_index % 2

            card, bottom = self.create_layout(self.container, card_type=room)
            card.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

            self.add_card(card)

            card_index +=1

            if room == "kitchen":
                var = tk.StringVar(value=upgrades[0]["option"])
                self.kitchen_var = var
            
                def radio_ticked(var=var, upgrades=upgrades):
                    selected = next(item for item in upgrades if item["option"] == var.get())
                    selections["kitchen"] = selected
                    self.total_price()


                selections["kitchen"] = upgrades[0]
                
                for item in upgrades:
                    option = ctk.CTkRadioButton(bottom, text=f"{item["text"]} (${item["price"]})", text_color="black", variable=var, value=item["option"], command=radio_ticked)
                    option.pack(anchor="w", padx=20, pady=2)

            else:
                for item in upgrades:
                    var = tk.BooleanVar(value=False)
                    self.check_vars.append(var)

                    option = ctk.CTkCheckBox(bottom, text=f"{item["text"]} (${item["price"]})", text_color="black", variable=var, command=lambda item=item, var=var: self.checkbox_ticked(item, var))
                    option.pack(anchor="w", padx=20, pady=2)

        self.create_int_card(ADDITIONS)

    def checkbox_ticked(self, item, var):
        key = (item["option"], item["text"])
        if var.get():
            selections[key] = item
        else:
            selections.pop(key, None)
        self.total_price()
    
    def show_about(self):

        errormsg = ctk.CTkToplevel(self.root)
        errormsg.title("ABOUT")
        errormsg.geometry("350x200")
        errormsg.configure(fg_color="white")

        title = ctk.CTkLabel(errormsg, text="About", text_color="#033805", font=("Georgia", 24, "bold"))
        title.pack(anchor="center", pady=20)
        
        description = ctk.CTkLabel(errormsg, text="The Waimak Build Co is a local company that supply a range of flatpack houses to the building trade and to retail customers. These are supplied as a kit that the customer then assembles themselves. The kit offers limited scope for customisation, to keep the cost as low as possible.", text_color="black", justify="center", wraplength=280)
        description.pack(anchor="center", padx=10)

        

    
    def open_signin(self):
        SigninWindow(self.root, members, self)
    
    def on_click(self):
        SignupWindow(self.root, members)

    def create_card(self):
        banner = ctk.CTkFrame(self.scroll_frame, fg_color="white", height=400)
        banner.pack(fill="x", padx=30, pady=(0,10))
        banner.pack_propagate(False)

        title = ctk.CTkLabel(banner, text="Waimak Builders Co", text_color="#033805", font=("Georgia", 44, "bold"))
        title.pack(expand=True)

        self.auth_buttons = ctk.CTkFrame(banner, fg_color="transparent")
        self.auth_buttons.place(relx=1.0, y=10, anchor="ne")

        self.signin_btn = ctk.CTkButton(self.auth_buttons, text="Sign In", command=self.open_signin)
        self.signin_btn.pack(side="right", padx=5, pady=5)

        self.signup_btn = ctk.CTkButton(self.auth_buttons, text="Sign Up", command=self.on_click)
        self.signup_btn.pack(side="right", padx=5, pady=5)

        self.about_btn = ctk.CTkButton(self.auth_buttons, text="About", command=self.show_about)
        self.about_btn.pack(side="right", padx=5, pady=5)

        self.user_buttons = ctk.CTkFrame(banner, fg_color="transparent")
        self.user_buttons.pack_forget()

        self.cart_btn = ctk.CTkButton(self.user_buttons, text="Receipts", command=self.open_cart)
        self.cart_btn.pack(side="left", padx=5)

        self.account_btn = ctk.CTkButton(self.user_buttons, text="Account", command=self.open_account)
        self.account_btn.pack(side="right", padx=5)

        self.signout_btn = ctk.CTkButton(self.user_buttons, text="Sign Out", command=self.sign_out)
        self.signout_btn.pack(side="right", padx=5)

        self.about_btn = ctk.CTkButton(self.user_buttons, text="About", command=self.show_about)
        self.about_btn.pack(side="right", padx=5, pady=5)

        top_border = ctk.CTkFrame(self.scroll_frame, height=2, fg_color="#FFD700")
        top_border.pack(side="top", fill="x")

        default_bar = ctk.CTkFrame(self.scroll_frame, fg_color="white")
        default_bar.pack(fill="x", pady=(0,10))
        default_bar.pack_propagate(False)

        top_border2 = ctk.CTkFrame(self.scroll_frame, height=2, fg_color="#FFD700")
        top_border2.pack(side="top", fill="x")

        d_settings = ctk.CTkLabel(default_bar, text="The basic kit costs $75,000 inclusive of taxes and delivery, and measures 8m x 8m. It includes a basic but functional bathroom, 2 bedrooms, a ‘standard’ fitted kitchen with space for a washing machine or dishwasher and a living room. All windows are double glazed, walls, floor and loft insulated to NZ standards. All rooms come with 1 double electrical socket as standard.", text_color="black", justify="left", wraplength=300)
        d_settings.grid(row=0, column=0, pady=30, padx=30)

        #talk about garbage collecting 

        img1 = ctk.CTkImage(light_image=Image.open("house.png"), dark_image=Image.open("house.png"), size=(220, 150))
        d_img1 = ctk.CTkLabel(default_bar, image=img1, text="")
        d_img1.grid(row=0, column=1, pady=10, padx=10)

        img2 = ctk.CTkImage(light_image=Image.open("floorplan.png"), dark_image=Image.open("floorplan.png"), size=(220, 150))
        d_img2 = ctk.CTkLabel(default_bar, image=img2, text="")
        d_img2.grid(row=0, column=2, pady=10, padx=10)

        self.default_images = [img1, img2]


    def create_layout(self, container, card_type):
        image_paths = {
            "kitchen": "tiny-house-kitchen-design.jpg",
            "bathroom": "bathroom.avif",
            "living room": "living room.jpg",
            "Sockets": "socket.webp",
            "Bedrooms": "heat pump.webp",
            "Network Points": "new work pts.jpg",
        }

        card = ctk.CTkFrame(container, fg_color="white", border_width=2, border_color="#FFD700", corner_radius=18)

        path = image_paths.get(card_type)
        if path:
            pil_img = Image.open(path)
            img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(400, 200))

            image_label = ctk.CTkLabel(card, image=img, text="", corner_radius=18)
            image_label.pack(fill="both", expand=True, padx=12, pady=(12, 0))

            if not hasattr(self, "images"):
                self.images = []
            self.images.append(img)
            
        bottom = ctk.CTkFrame(card, fg_color="#ededed")
        bottom.pack(fill="both", expand=True, padx=12, pady=12)

        title = ctk.CTkLabel(bottom, text=card_type.upper(), text_color="#033805", font=("Georgia", 18, "bold"))
        title.pack(anchor="w", padx=15, pady=10)

        return card, bottom

    def create_int_card(self, ADDITIONS):
        card_index = self.card_index
        for key, values in ADDITIONS.items():
            row = card_index // 2
            column = card_index % 2

            card, bottom = self.create_layout(self.container, card_type=key)
            card.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

            self.add_card(card)

            card_index +=1

            if key == "Sockets":
                lbl = ctk.CTkLabel(bottom, text="The maximum number of extra sockets in the build is 12 (1G + 2G total)", text_color="black", justify="left", wraplength=350)
                lbl.pack(anchor="w", padx=10)
            elif key == "Network Points":
                lbl = ctk.CTkLabel(bottom, text="Requires the addition of a loft mounted 8 port 10/100/1000 network switch ($100)", text_color="black", justify="left", wraplength=350)
                lbl.pack(anchor="w", padx=10)

            for item in values:

                controls = ctk.CTkFrame(bottom, fg_color="transparent")
                controls.pack(fill="x")

                sub_key = item["name"]
                sub_value = item["value"]
                price = item["price"]

                key_label = ctk.CTkLabel(controls, text=f"{sub_key} (${price})", text_color="black")
                key_label.pack(side="left", padx=10)

                value_label = ctk.CTkLabel(controls, text=str(sub_value), text_color="black")
                value_label.pack(side="left", padx=10)

                self.value_labels.append((item, value_label))

                plus_btn = ctk.CTkButton(controls, text="+", height=10, width=10, corner_radius=50, command=lambda item=item, vlabel=value_label: self.plus_btn_action(item, vlabel))
                plus_btn.pack(side="left", padx=10, pady=5)

                minus_btn = ctk.CTkButton(controls, text="-", height=10, width=10, corner_radius=50, command=lambda item=item, vlabel=value_label: self.minus_btn_action(item, vlabel))
                minus_btn.pack(side="left", padx=10, pady=5)

        self.card_index = card_index

    def plus_btn_action(self, item, value_label):

        current_value = item["value"]
        new_value = current_value + 1

        for category, values in ADDITIONS.items():

            if item in values:

                total = sum(dictionary["value"] for dictionary in values)

                if category == "Sockets":
                    limit = 12

                elif category == "Bedrooms":
                    limit = 2

                elif category == "Network Points":
                    limit = 8

                if total >= limit:
                    value_label.configure(text=f"{current_value} maximum limit reached", text_color="black")
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

                if category == "Sockets":
                    minimum = 1

                elif category == "Bedrooms":
                    minimum = 0

                elif category == "Network Points":
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

        lbl.configure(text=f"Total price: ${total:,.2f}", text_color="black")

        return total

class SignupWindow(ctk.CTkToplevel):
    def __init__(self, root, members, username=None, layout=None):
        super().__init__(root)

        self.members = members
        self.new_member = {}
        self.username = username
        self.layout = layout
        self.editing_member = None
        
        if username is not None:
            self.editing_member = next((member for member in self.members if member.get("username") == username), None)
            if self.editing_member is None:
                raise ValueError(f"No member found for username: {username}")
            
        self.title("SIGN UP")
        self.geometry("320x650")
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        

        self.valid_first = ctk.BooleanVar(value=False)
        self.valid_last = ctk.BooleanVar(value=False)
        self.valid_email_var = ctk.BooleanVar(value=False)
        self.valid_phone = ctk.BooleanVar(value=False)
        self.valid_user = ctk.BooleanVar(value=False)
        self.valid_pass = ctk.BooleanVar(value=False)
        self.valid_company = ctk.BooleanVar(value=True)

        self.make_sheet()
    
    def prefill_fields(self):
        member = self.editing_member

        self.fname.insert(0, member.get("name", {}).get("first", ""))
        self.lname.insert(0, member.get("name", {}).get("last", ""))
        self.email.insert(0, member.get("email", ""))

        phone = member.get("phone", "")

        if " " in phone:
            area, number = phone.split(" ", 1)
            self.area_dropdown.set(f"({area})")
            self.phone.insert(0, number)

        self.username.insert(0, member.get("username", ""))

        if member.get("company"):
            self.check_trader.set("on")
            self.valid_trader()
            self.company_name.insert(0, member["company"])
            self.save_comp()
        
        self.password.insert(0, member.get("password", ""))
        self.valid_password(None)

        self.valid_name(self.fname, self.lbl1, self.valid_first)
        self.valid_name(self.lname, self.lbl2, self.valid_last)
        self.valid_email()
        self.valid_number()

        self.valid_user.set(True)
        self.lbl5.configure(text="Username", text_color="gray")

        self.update_check_button()

    def make_sheet(self):
        # First name Labels and Entries
        self.lbl1 = ctk.CTkLabel(self, text="First Name", anchor="w")
        self.lbl1.grid(row=0, column=1, sticky="w", padx=10)
        self.fname = ctk.CTkEntry(self, placeholder_text="Enter firstname", height=40)
        self.fname.grid(row=1, column=1, columnspan=2, sticky="ew", padx=10)

        # Last name Labels and Entries
        self.lbl2 = ctk.CTkLabel(self, text="Last Name", anchor="w")
        self.lbl2.grid(row=2, column=1, sticky="w", padx=10)
        self.lname = ctk.CTkEntry(self, placeholder_text="Enter lastname", height=40)
        self.lname.grid(row=3, column=1, columnspan=2, sticky="ew", padx=10)

        # Email Labels and Entries
        self.lbl3 = ctk.CTkLabel(self, text="Email Address", anchor="w")
        self.lbl3.grid(row=4, column=1, sticky="w", padx=10)
        self.email = ctk.CTkEntry(self, placeholder_text="Enter email address", height=40)
        self.email.grid(row=5, column=1, columnspan=2, sticky="ew", padx=10)

        # Selecting Area Codes 
        def chosen_area(choice):
            self.selected_country.set(choice)

            area = choice.split("(")[1].replace(")", "")
            self.area_dropdown.set(f"({area})")

        self.selected_country = ctk.StringVar()

        # Phone Number Labels and Entries
        self.lbl4 = ctk.CTkLabel(self, text="Phone Number", anchor="w")
        self.lbl4.grid(row=6, column=1, columnspan=2, sticky="w", padx=10)
        self.area_dropdown = ctk.CTkComboBox(self, values=country_codes, state="readonly", height=40, command=chosen_area)
        self.area_dropdown.set("(+64)")
        self.selected_country.set("New Zealand (+64)")
        self.area_dropdown.grid(row=7, column=1, sticky="ew", padx=(10, 5))
        self.phone = ctk.CTkEntry(self, placeholder_text="Enter Phone Number", height=40)
        self.phone.grid(row=7, column=2, sticky="ew", padx=(5, 10))

        # Username Labels and Entries
        self.lbl5 = ctk.CTkLabel(self, text="Username", anchor="w")
        self.lbl5.grid(row=8, column=1, columnspan=2, sticky="w", padx=10)
        self.username = ctk.CTkEntry(self, placeholder_text="Username", height=40)
        self.username.grid(row=9, column=1, columnspan=2, sticky="ew", padx=10) 

        # Checking quality of Password
        self.password_rules = []
        self.checked_var = []

        for position, rule in enumerate(contain):
            row = position + 12

            var = ctk.IntVar()
            self.checked_var.append(var)

            self.lbl_rule = ctk.CTkCheckBox(self, text=rule, variable=var, text_color="gray", state="disabled", border_width=1, font=("Arial", 10), checkbox_width=16, checkbox_height=16)
            self.lbl_rule.grid(row=row, column=1, columnspan=2, sticky="ew", padx=10)

            self.password_rules.append(self.lbl_rule)

        # Password Labels and Entries
        self.lbl6 = ctk.CTkLabel(self, text="Password", anchor="w")
        self.lbl6.grid(row=10, column=1, sticky="w", padx=10)
        self.password = ctk.CTkEntry(self, placeholder_text="Password", height=40)
        self.password.grid(row=11, column=1, columnspan=2, sticky="ew", padx=10)
        self.password.bind("<KeyRelease>", self.valid_password)

        self.new_row = len(self.password_rules) + 12

        # Traders Labels and Entries if they choose that 
        self.check_trader = ctk.StringVar(value="off")
        self.trader = ctk.CTkCheckBox(self, text="I am a Trade Customer", command=self.valid_trader, variable=self.check_trader, onvalue="on", offvalue="off")
        self.trader.grid(row=self.new_row, column=1, columnspan=2, sticky="ew", padx=10, pady=10)
        self.discount = ctk.CTkLabel(self, text="Trade Customers receive a 10% discount on both the basic house and any options selected", text_color="gray", font=("Arial", 10), wraplength=300, justify="left", anchor="w")
        self.company = ctk.CTkLabel(self, text="Company")
        self.company_name = ctk.CTkEntry(self, placeholder_text="Enter company name here", height=40)

        # Check to see if the information provided in the functions is valid
        self.check = ctk.CTkButton(self, text="Check", height=40, state="disabled", fg_color="gray", command=self.accept_new_user)
        self.check.grid(row=(self.new_row + 4), column=1, columnspan=2, sticky="ew", padx=10, pady=10)
        
        #why i chose focus out instead of key release and how this works
        self.fname.bind("<FocusOut>", lambda event: self.valid_name(self.fname, self.lbl1, self.valid_first))
        self.lname.bind("<FocusOut>", lambda event: self.valid_name(self.lname, self.lbl2, self.valid_last))
        self.email.bind("<FocusOut>", lambda event: self.valid_email())
        self.phone.bind("<FocusOut>", lambda event: self.valid_number())
        self.username.bind("<FocusOut>", lambda event: self.valid_username())
        self.company_name.bind("<KeyRelease>", lambda event: self.save_comp())

        if self.editing_member:
            self.prefill_fields()
            self.check.configure(text="Update", command=self.accept_new_user)
        else:
            self.check.configure(text="Sign Up", command=self.accept_new_user)

    def valid_number(self):
            area = self.area_dropdown.get()
            phone_entry = self.phone.get().strip()

            if not phone_entry:
                self.lbl4.configure(text="PHONE NUMBER REQUIRED", text_color="red")
                self.valid_phone.set(False)
            elif phone_entry.isdigit():
                self.lbl4.configure(text="Phone Number", text_color="gray")
                full_num = f"{area} {phone_entry}"
                self.new_member["phone"] = full_num
                self.valid_phone.set(True)

            else:
                self.lbl4.configure(text="NUMERIC NUMBER ONLY", text_color="red")
                self.valid_phone.set(False)
                

            self.update_check_button()


    def valid_email(self):
        email_match = self.email.get().strip()
        #talk about finding this and what it does
        email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        #also talk about re.fullmatch()
        if not re.fullmatch(email_pattern, email_match):
            self.lbl3.configure(text="INVALID EMAIL", text_color="red")
            self.valid_email_var.set(False)

        elif any(member.get("email") == email_match for member in self.members if member is not self.editing_member):
            self.lbl3.configure(text="EMAIL ALREADY IN USE", text_color="red")
            self.valid_email_var.set(False)

        else:
            self.lbl3.configure(text="Email", text_color="gray")
            self.valid_email_var.set(True)

        self.update_check_button()


    def valid_name(self, entry, label, valid_var):
        name = entry.get().strip()

        if any(char.isdigit() for char in name):
            label.configure(text="INVALID NAME", text_color="red")
            valid_var.set(False)

        elif not name:
            label.configure(text="NAME REQUIRED", text_color="red")
            valid_var.set(False)

        else:
            if label == self.lbl1:
                label.configure(text="First Name", text_color="gray")
                valid_var.set(True)

            elif label == self.lbl2:
                label.configure(text="Last Name", text_color="gray")
                valid_var.set(True)

        self.update_check_button()


    def valid_username(self):
        check_user = self.username.get()

        if not check_user:
            self.lbl5.configure(text="USERNAME REQUIRED", text_color="red")
            self.valid_user.set(False)

        elif any(member.get("username") == check_user for member in self.members if member is not self.editing_member):            
            self.lbl5.configure(text="USERNAME ALREADY IN USE", text_color="red")
            self.valid_user.set(False)

        else:
            self.lbl5.configure(text="Username", text_color="gray")
            self.valid_user.set(True)

        self.update_check_button()



    def valid_password(self, event):
        check_pass = self.password.get()

        if check_pass:
            self.password_rules[0].select()
        else:
            self.password_rules[0].deselect()
            
        if len(check_pass) > 5:
            self.password_rules[1].select()
        else:
            self.password_rules[1].deselect()

        if any(not char.isalnum() and not char.isspace() for char in check_pass):
            self.password_rules[2].select()
        else:
            self.password_rules[2].deselect()

        if any(char.isupper() for char in check_pass):
            self.password_rules[3].select()
        else:
            self.password_rules[3].deselect()

        if any(char.isdigit() for char in check_pass):
            self.password_rules[4].select()
        else:
            self.password_rules[4].deselect()

        
        if all(var.get() == 1 for var in self.checked_var):
            for rule in self.password_rules:
                rule.grid_forget()
            
            self.lbl6.configure(text="Password", text_color="gray")
            self.valid_pass.set(True)

        else:
            for position, rule in enumerate(self.password_rules):
                rule.grid(row=position + 12, column=1, columnspan=2, padx=10, sticky="w")

            self.lbl6.configure(text="INVALID PASSWORD", text_color="red")
            self.valid_pass.set(False)

        self.update_check_button()
            
    
    def valid_trader(self):
        if self.check_trader.get() == "on":
            self.geometry("320x730")
            self.discount.grid(row=(self.new_row + 1), column=1, sticky="w", padx=10, columnspan=2)
            self.company.grid(row=(self.new_row + 2), column=1, sticky="w", padx=10)
            self.company_name.grid(row=(self.new_row + 3), column=1, columnspan=2, sticky="ew", padx=10)
        
        elif self.check_trader.get() == "off":
            self.geometry("320x650")
            self.discount.grid_forget()
            self.company.grid_forget()
            self.company_name.grid_forget()
        
        self.save_comp()
    

    def save_comp(self):
        company_entry = self.company_name.get()

        if self.check_trader.get() == "on":
            if company_entry:
                self.company.configure(text="Company", text_color="gray")
                self.valid_company.set(True)
            else:
                self.company.configure(text="COMPANY REQUIRED", text_color="red")
                self.valid_company.set(False)
        else:
            self.valid_company.set(True)

        self.update_check_button()

    def update_check_button(self):
        if not hasattr(self, "check"):
            return
        
        is_valid = all((
            self.valid_first.get(),
            self.valid_last.get(),
            self.valid_email_var.get(),
            self.valid_phone.get(),
            self.valid_user.get(),
            self.valid_pass.get(),
            self.valid_company.get(),
        ))
        if is_valid: 
            self.check.configure(state="normal", fg_color="green") 
        else: 
            self.check.configure(state="disabled", fg_color="gray") 


    def open_msg(self, editing_member):
            errormsg = ctk.CTkToplevel(self.master)
            errormsg.title("Success")

            if editing_member == None:
                error_lbl = ctk.CTkLabel(errormsg, text="New account added successfully!")
                error_lbl.pack()

            else: 
                error_lbl = ctk.CTkLabel(errormsg, text="Account updated successfully!")
                error_lbl.pack()

            errormsg.after(3000, errormsg.destroy)

            self.destroy()


    def accept_new_user(self):

        updated_member = {
            "name": {
                "first": self.fname.get().strip().capitalize(),
                "last": self.lname.get().strip().capitalize(),
            },
            "email": self.email.get().strip(),
            "phone": f"{self.area_dropdown.get()} {self.phone.get().strip()}",
            "username": self.username.get().strip(),
            "password": self.password.get(),
        }

        if self.check_trader.get() == "on":
            updated_member["company"] = self.company_name.get().strip()

        if self.editing_member is not None:
            self.editing_member.clear()
            self.editing_member.update(updated_member)
            self.open_msg(self.editing_member)
            print(members)
        
        else:

            self.new_member["name"] = {
                "first": self.fname.get().capitalize(),
                "last": self.lname.get().capitalize()
            }

            self.new_member["email"] = self.email.get()

            area = self.area_dropdown.get()
            self.new_member["phone"] = f"{area} {self.phone.get().strip()}"

            self.new_member["username"] = self.username.get()
            self.new_member["password"] = self.password.get()

            if self.check_trader.get() == "on":
                self.new_member["company"] = self.company_name.get()

            members.append(self.new_member.copy())
            self.open_msg(None)
            print(members)


class SigninWindow(ctk.CTkToplevel):
    def __init__(self, root, members, layout):
        super().__init__(root)
        self.layout = layout
        self.members = members
        self.current_user = ""

        self.title("SIGN IN")
        self.geometry("320x200")

        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.create_window()
    
    def create_window(self):
        self.lbl5 = ctk.CTkLabel(self, text="Username", anchor="w")
        self.lbl5.grid(row=0, column=1, sticky="w", padx=10)

        self.username = ctk.CTkEntry(self, placeholder_text="Username", height=40)
        self.username.grid(row=1, column=1, columnspan=2, sticky="ew", padx=10)
        self.username.bind("<KeyRelease>", self.filled_in)

        self.lbl6 = ctk.CTkLabel(self, text="Password", anchor="w")
        self.lbl6.grid(row=2, column=1, sticky="w", padx=10)

        self.password = ctk.CTkEntry(self, placeholder_text="Password", height=40)
        self.password.grid(row=3, column=1, columnspan=2, sticky="ew", padx=10)
        self.password.bind("<KeyRelease>", self.filled_in)
            
        self.check = ctk.CTkButton(self, text="Check", height=40, state="disabled", fg_color="gray", command=self.check_user)
        self.check.grid(row=4, column=1, columnspan=2, sticky="ew", padx=10, pady=10)

    def check_user(self):
        input_user = self.username.get()
        input_pass = self.password.get()

        if any(input_user == member["username"] and input_pass == member["password"] for member in self.members):
            self.layout.current_user = input_user
            self.layout.show_signed_in()

            errormsg = ctk.CTkToplevel(self.master)
            errormsg.title("Success")

            error_lbl = ctk.CTkLabel(errormsg, text=f"Welcome back {input_user}")
            error_lbl.pack()

            errormsg.after(3000, errormsg.destroy)

            self.destroy()

        else:
            errormsg = ctk.CTkToplevel(self.master)
            errormsg.title("Unsuccessful")

            error_lbl = ctk.CTkLabel(errormsg, text="Incorrect password or username")
            error_lbl.pack()

            errormsg.after(3000, errormsg.destroy)

    def filled_in(self, event):
        if self.password.get() and self.username.get():
            self.check.configure(state="normal", fg_color="green")
            self.lbl5.configure(text="Username", text_color="gray")
            self.lbl6.configure(text="Password", text_color="gray")
        else:
            self.check.configure(state="disabled", fg_color="gray")
            if not self.username.get():
                self.lbl5.configure(text="USERNAME REQUIRED", text_color="red")
            if not self.password.get():
                self.lbl6.configure(text="PASSWORD REQUIRED", text_color="red")

class AccountWindow(ctk.CTkToplevel):
    def __init__(self, root, username, members, layout):
        super().__init__(root)
        self.layout = layout
        self.members = members
        self.username = username

        SignupWindow(root, members, username=username, layout=layout)
        self.destroy()
       


class ReceiptsWindow(ctk.CTkToplevel):
    def __init__(self, root, purchaces, username, layout):
        super().__init__(root)
        self.layout = layout
        self.purchaces = purchaces
        self.username = username

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.scroll_rec = ctk.CTkScrollableFrame(self)
        self.scroll_rec.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.geometry("500x400")
        self.title("RECEIPTS")

        self.create_receipts_window()
    
    def create_receipts_window(self):

        signed_in_user = self.username

        if not purchaces.get(signed_in_user):
            self.msg = ctk.CTkLabel(self.scroll_rec, text="You have made no purchaces yet")
            self.msg.grid()
            return


        else:
            row = 0
            for house, choices in enumerate(self.purchaces[signed_in_user], start=1):

                self.title = ctk.CTkLabel(self.scroll_rec, text=f"------- Receipt No.{house} -------")
                self.title.grid(sticky="new", row=row, columnspan=2)

                row += 1

                self.lbl1 = ctk.CTkLabel(self.scroll_rec, text="Default Settings")
                self.lbl1.grid(column=0, row=row, sticky="w", padx=10)
            
                self.price1 = ctk.CTkLabel(self.scroll_rec, text="$74,860.00")
                self.price1.grid(column=1, row=row, sticky="e", padx=10)

                row += 1

                total_price = 75000

                for category, items in choices.items():

                    for item in items:
                        if "text" in item:
                            lbl = ctk.CTkLabel(self.scroll_rec, text=f'{item["option"]}: {item["text"]} ({category})')
                            lbl.grid(row=row, column=0, sticky="w", padx=10)

                            price = item["price"]

                            lbl_price = ctk.CTkLabel(self.scroll_rec, text=f"${price:,.2f}")
                            lbl_price.grid(row=row, column=1, sticky="e", padx=10)

                            total_price += price
                            row += 1

                        elif "value" in item:
                            lbl = ctk.CTkLabel(self.scroll_rec, text=f'{item["value"]} x {item["name"]} ({category})')
                            lbl.grid(row=row, column=0, sticky="w", padx=10)

                            price = item["value"] * item["price"]

                            lbl_price = ctk.CTkLabel(self.scroll_rec, text=f"${price:,.2f}")
                            lbl_price.grid(row=row, column=1, sticky="e", padx=10)

                            total_price += price
                            row += 1

                            if category == "Network Points" and item["value"] > 2:
                                lbl = ctk.CTkLabel(self.scroll_rec, text="Loft mounted 8 port 10/100/1000 network switch")
                                lbl.grid(row=row, column=0,sticky="w", padx=10)

                                lbl_price = ctk.CTkLabel(self.scroll_rec, text=f"$100")
                                lbl_price.grid(row=row, column=1, sticky="e", padx=10)

                                total_price += 100
                                row += 1 


                for member in members:
                    if member["username"] == signed_in_user:

                        if "company" in member:

                            discount_value = total_price * 0.1
                            discount_price = total_price - discount_value

                            lbl_discount = ctk.CTkLabel(self.scroll_rec, text="10% discount")
                            lbl_discount.grid(row=row, column=0, sticky="w", padx=10)

                            lbl_discount_price = ctk.CTkLabel(self.scroll_rec, text=f"${discount_value:,.2f}")
                            lbl_discount_price.grid(row=row, column=1, sticky="e", padx=10)

                            total_price = discount_price
                            row += 1

                        break
                total_price -= 140

                lbl_line = ctk.CTkLabel(self.scroll_rec, text="----------------------------------------------------------------------")
                lbl_line.grid(row=row, column=0, columnspan=2, sticky="new", padx=10)

                row += 1

                lbl_total = ctk.CTkLabel(self.scroll_rec, text="Total Price:")
                lbl_total.grid(row=row, column=0, sticky="w", padx=10, pady=(0, 20))

                lbl_total_price = ctk.CTkLabel(self.scroll_rec, text=f"${total_price:,.2f}")
                lbl_total_price.grid(row=row, column=1, sticky="e", padx=10, pady=(0, 10))

                row +=1

                cancel_btn = ctk.CTkButton(self.scroll_rec, text=f"Cancel Order No.{house}", command=lambda house=house: self.cancel_order(house))
                cancel_btn.grid(row=row, column=0, columnspan=2, pady=(0, 20))

                row += 2
    def cancel_order(self, house):

        self.purchaces[self.username].pop(house - 1)

        for widget in self.scroll_rec.winfo_children():
            widget.destroy()

        self.create_receipts_window()



root = ctk.CTk()

lbl = ctk.CTkLabel(root, text="Total price: $75,000.00")
lbl.pack(side="bottom", pady=10)

Layout(root)


root.mainloop()
