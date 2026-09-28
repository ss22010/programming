import customtkinter as ctk
from tkinter import *
import re

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

contain = [
    "Password required",
    "Must be greater than 5 characters long", 
    "Must contain one or more special charcaters",
    "Must contain one or more capital letters",
    "Must contain one or more numbers"
]

new_member = {}

root = ctk.CTk()

def on_click():
    new_window = ctk.CTkToplevel(master=root)
    new_window.title("add_acc_win")
    new_window.geometry("700x500")

    new_window.after(200, lambda: new_window.focus())

    lbl1 = ctk.CTkLabel(new_window, text="First Name", height=50, width=100)
    lbl1.grid(row=0, column=0)
    fname = ctk.CTkEntry(new_window, placeholder_text="Enter firstname", width=100, height=50)
    fname.grid(row=0, column=1)


    lbl2 = ctk.CTkLabel(new_window, text="Last Name", height=50, width=100)
    lbl2.grid(row=1, column=0)
    lname = ctk.CTkEntry(new_window, placeholder_text="Enter lastname", width=100, height=50)
    lname.grid(row=1, column=1)


    lbl3 = ctk.CTkLabel(new_window, text="Email Address", height=50, width=100)
    lbl3.grid(row=2, column=0)
    email = ctk.CTkEntry(new_window, placeholder_text="Enter email address", width=100, height=50)
    email.grid(row=2, column=1)

    lbl4 = ctk.CTkLabel(new_window, text="Phone Number", height = 50, width=100)
    lbl4.grid(row=3, column=0)
    area_dropdown = ctk.CTkComboBox(new_window, values=country_codes, width=180, state="readonly")
    area_dropdown.set("New Zealand (+64)")
    area_dropdown.grid(row=3, column=1, padx=(5, 5))

    phone = ctk.CTkEntry(new_window, placeholder_text="Enter Phone Number", width=200)
    phone.grid(row=3, column=2, padx=(5, 0))

    lbl5 = ctk.CTkLabel(new_window, text="Username", height=50, width=100)
    lbl5.grid(row=4, column=0)
    username = ctk.CTkEntry(new_window, placeholder_text="Username", width=200)
    username.grid(row=4, column=1)

    def valid_number():
        selected_text = area_dropdown.get()

        try:
            #explain how this works and used 
            area = selected_text.split("(")[1].replace(")", "")
        except IndexError:
            area = ""

        phone_entry = phone.get().strip()

        if not phone_entry:
            lbl4.configure(text="Please Enter Your Phone Number")
        else:
            full_num = f"{area} {phone_entry}"
            lbl4.configure(text="VALID PHONE NUMBER")
            print(f"Clean number: {full_num}")


    def valid_email():
        email_match = email.get()
        #talk about finding this and what it does
        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

        #also talk about re.fullmatch()
        if re.fullmatch(email_pattern, email_match):
            lbl3.configure(text="VALID EMAIL")
        else:
            lbl3.configure(text="INVALID EMAIL")

    def valid_name(entry, label):
        name = entry.get()

        if any(char.isdigit() for char in name):
            label.configure(text="INVALID NAME")
        elif not name:
            label.configure(text="NAME REQUIRED")
        else:
            label.configure(text="VALID NAME")

    def valid_username():
        check_user = username.get()

        if not check_user:
            lbl5.configure(text="USERNAME REQUIRED")
        elif check_user in new_member:
            lbl5.configure(text="USERNAME UNAVALIBLE")
        else:
            lbl5.configure(text="VALID USERNAME")

    def valid_password(event):
        check_pass = password.get()

        if check_pass:
            password_rules[0].select()
            password_rules[0].configure(text_color="green")
        else:
            password_rules[0].deselect()
            password_rules[0].configure(text_color="gray")

            
        if len(check_pass) > 5:
            password_rules[1].select()
            password_rules[1].configure(text_color="green")
        else:
            password_rules[1].deselect()
            password_rules[1].configure(text_color="gray")

        if any(not char.isalnum() and not char.isspace() for char in check_pass):
            password_rules[2].select()
            password_rules[2].configure(text_color="green")
        else:
            password_rules[2].deselect()
            password_rules[2].configure(text_color="gray")

        if any(char.isupper() for char in check_pass):
            password_rules[3].select()
            password_rules[3].configure(text_color="green")
        else:
            password_rules[3].deselect()
            password_rules[3].configure(text_color="gray")

        if any(char.isdigit() for char in check_pass):
            password_rules[4].select()
            password_rules[4].configure(text_color="green")
        else:
            password_rules[4].deselect()
            password_rules[4].configure(text_color="gray")
        
        if all(var.get() == 1 for var in checked_var):
            for rule in password_rules:
                rule.grid_forget()
            
            lbl.grid(row=7, column=0)

        else:
            lbl.grid_forget()
            for position, rule in enumerate(password_rules):
                rule.grid(row=position + 7, column=0, sticky="w")
            

    password_rules = []
    checked_var = []
    for position, rule in enumerate(contain):
        row = position + 7
        var = ctk.IntVar()
        checked_var.append(var)
    
        lbl_rule = ctk.CTkCheckBox(new_window, text=rule, variable=var, text_color="gray", state="disabled")
        lbl_rule.grid(row=row, column=0, sticky="w")

        password_rules.append(lbl_rule)
        
    lbl = ctk.CTkLabel(new_window, text="VALID PASSWORD")

    password = ctk.CTkEntry(new_window, placeholder_text="Password", width=200)
    password.grid(row=5, column=1)

    password.bind("<KeyRelease>", valid_password)


    check = ctk.CTkButton(new_window, text="Check", command=lambda fname=fname, lname=lname, lbl1=lbl1, lbl2=lbl2: [valid_name(fname, lbl1), valid_name(lname, lbl2), valid_email(), valid_number(), valid_username(), valid_password()])
    check.grid(row=6, column=1)


btn = ctk.CTkButton(root, text="add_account", command=on_click)
btn.pack()

root.mainloop()