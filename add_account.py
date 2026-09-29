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

members = [{
    "name": {
        "first": "Sarah",
        "last": "Shaw"
    },
    "email": "123@gmail.com",
    "phone": "+64 0278293321",
    "username": "sarahs123",
    "password": "123!@#QWE"
}]


root = ctk.CTk()

def on_click():
    new_window = ctk.CTkToplevel(root)
    new_window.title("SIGN UP")
    new_window.geometry("320x650")

    new_window.columnconfigure(1, weight=1)
    new_window.columnconfigure(2, weight=1)

    valid_first = ctk.BooleanVar(value=False)
    valid_last = ctk.BooleanVar(value=False)
    valid_email_var = ctk.BooleanVar(value=False)
    valid_phone = ctk.BooleanVar(value=False)
    valid_user = ctk.BooleanVar(value=False)
    valid_pass = ctk.BooleanVar(value=False)
    valid_company = ctk.BooleanVar(value=True) 

    

    new_member = {}

    lbl1 = ctk.CTkLabel(new_window, text="First Name", anchor="w")
    lbl1.grid(row=0, column=1, sticky="w", padx=10)

    fname = ctk.CTkEntry(new_window, placeholder_text="Enter firstname", height=40)
    fname.grid(row=1, column=1, columnspan=2, sticky="ew", padx=10)


    lbl2 = ctk.CTkLabel(new_window, text="Last Name", anchor="w")
    lbl2.grid(row=2, column=1, sticky="w", padx=10)
    lname = ctk.CTkEntry(new_window, placeholder_text="Enter lastname", height=40)
    lname.grid(row=3, column=1, columnspan=2, sticky="ew", padx=10)


    lbl3 = ctk.CTkLabel(new_window, text="Email Address", anchor="w")
    lbl3.grid(row=4, column=1, sticky="w", padx=10)
    email = ctk.CTkEntry(new_window, placeholder_text="Enter email address", height=40)
    email.grid(row=5, column=1, columnspan=2, sticky="ew", padx=10)

    def chosen_area(choice):
        selected_country.set(choice)

        area = choice.split("(")[1].replace(")", "")
        area_dropdown.set(f"({area})")
    
    lbl4 = ctk.CTkLabel(new_window, text="Phone Number", anchor="w")
    lbl4.grid(row=6, column=1, columnspan=2, sticky="w", padx=10)

    selected_country = ctk.StringVar()

    area_dropdown = ctk.CTkComboBox(new_window, values=country_codes, state="readonly", height=40, command=chosen_area)
    area_dropdown.set("(+64)")
    selected_country.set("New Zealand (+64)")
    area_dropdown.grid(row=7, column=1, sticky="ew", padx=(10, 5))


    phone = ctk.CTkEntry(new_window, placeholder_text="Enter Phone Number", height=40)
    phone.grid(row=7, column=2, sticky="ew", padx=(5, 10))

    lbl5 = ctk.CTkLabel(new_window, text="Username", anchor="w")
    lbl5.grid(row=8, column=1, sticky="w", padx=10)

    username = ctk.CTkEntry(new_window, placeholder_text="Username", height=40)
    username.grid(row=9, column=1, columnspan=2, sticky="ew", padx=10)

    def valid_number():
        area = area_dropdown.get()
        phone_entry = phone.get().strip()

        if not phone_entry:
            lbl4.configure(text="PHONE NUMBER REQUIRED", text_color="red")
            valid_phone.set(False)
        elif phone_entry.isdigit():
            lbl4.configure(text="Phone Number", text_color="gray")
            full_num = f"{area} {phone_entry}"
            new_member["phone"] = full_num
            valid_phone.set(True)

        else:
            lbl4.configure(text="NUMERIC NUMBER ONLY", text_color="red")
            valid_phone.set(False)
            

        update_check_button()

    def valid_email():
        email_match = email.get()
        #talk about finding this and what it does
        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

        #also talk about re.fullmatch()
        if re.fullmatch(email_pattern, email_match):
            lbl3.configure(text="Email", text_color="gray")
            valid_email_var.set(True)
        else:
            lbl3.configure(text="INVALID EMAIL", text_color="red")
            valid_email_var.set(False)
        update_check_button()

    def valid_name(entry, label, valid_var):
        name = entry.get().strip()

        if any(char.isdigit() for char in name):
            label.configure(text="INVALID NAME", text_color="red")
            valid_var.set(False)
        elif not name:
            label.configure(text="NAME REQUIRED", text_color="red")
            valid_var.set(False)
        else:
            if label == lbl1: 
                label.configure(text="First Name", text_color="gray")
                valid_var.set(True)

            elif label == lbl2:
                label.configure(text="Last Name", text_color="gray")
                valid_var.set(True)

        update_check_button()

    def valid_username():
        check_user = username.get()

        if not check_user:
            lbl5.configure(text="USERNAME REQUIRED", text_color="red")
            valid_user.set(False)

        elif any(member.get("username") == check_user for member in members):
            lbl5.configure(text="USERNAME UNAVAILABLE", text_color="red")
            valid_user.set(False)

        else:
            lbl5.configure(text="Username", text_color="gray")
            valid_user.set(True)

        update_check_button()

    def valid_password(event):
        check_pass = password.get()

        if check_pass:
            password_rules[0].select()
        else:
            password_rules[0].deselect()
            
        if len(check_pass) > 5:
            password_rules[1].select()
        else:
            password_rules[1].deselect()

        if any(not char.isalnum() and not char.isspace() for char in check_pass):
            password_rules[2].select()
        else:
            password_rules[2].deselect()

        if any(char.isupper() for char in check_pass):
            password_rules[3].select()
        else:
            password_rules[3].deselect()

        if any(char.isdigit() for char in check_pass):
            password_rules[4].select()
        else:
            password_rules[4].deselect()

        
        if all(var.get() == 1 for var in checked_var):
            for rule in password_rules:
                rule.grid_forget()
            
            lbl6.configure(text="Password", text_color="gray")
            valid_pass.set(True)

        else:
            for position, rule in enumerate(password_rules):
                rule.grid(row=position + 12, column=1, columnspan=2, padx=10, sticky="w")

            lbl6.configure(text="INVALID PASSWORD", text_color="red")
            valid_pass.set(False)

        update_check_button()
            
            

    password_rules = []
    checked_var = []

    for position, rule in enumerate(contain):
        row = position + 12

        var = ctk.IntVar()
        checked_var.append(var)

        lbl_rule = ctk.CTkCheckBox(new_window, text=rule, variable=var, text_color="gray", state="disabled", border_width=1, font=("Arial", 10), checkbox_width=16, checkbox_height=16)
        lbl_rule.grid(row=row, column=1, columnspan=2, sticky="ew", padx=10)

        password_rules.append(lbl_rule)


    lbl6 = ctk.CTkLabel(new_window, text="Password", anchor="w")
    lbl6.grid(row=10, column=1, sticky="w", padx=10)

    password = ctk.CTkEntry(new_window, placeholder_text="Password", height=40)
    password.grid(row=11, column=1, columnspan=2, sticky="ew", padx=10)


    password.bind("<KeyRelease>", valid_password)

    new_row = len(password_rules) + 12

    def valid_trader():
        if check_trader.get() == "on":
            new_window.geometry("320x730")
            discount.grid(row=(new_row + 1), column=1, sticky="w", padx=10, columnspan=2)
            company.grid(row=(new_row + 2), column=1, sticky="w", padx=10)
            company_name.grid(row=(new_row + 3), column=1, columnspan=2, sticky="ew", padx=10)
        elif check_trader.get() == "off":
            new_window.geometry("320x650")
            discount.grid_forget()
            company.grid_forget()
            company_name.grid_forget()
        save_comp()
    

    def save_comp():
        company_entry = company_name.get()

        if check_trader.get() == "on":
            if company_entry:
                company.configure(text="Company", text_color="gray")
                valid_company.set(True)
            else:
                company.configure(text="COMPANY REQUIRED", text_color="red")
                valid_company.set(False)
        else:
            valid_company.set(True)

        update_check_button()


    check_trader = ctk.StringVar(value="off")

    trader = ctk.CTkCheckBox(new_window, text="I am a Trade Customer", command=valid_trader, variable=check_trader, onvalue="on", offvalue="off")
    trader.grid(row=new_row, column=1, columnspan=2, sticky="ew", padx=10, pady=10)

    discount = ctk.CTkLabel(new_window, text="Trade Customers receive a 10% discount on both the basic house and any options selected", text_color="gray", font=("Arial", 10), wraplength=300, justify="left", anchor="w")
    company = ctk.CTkLabel(new_window, text="Company")
    company_name = ctk.CTkEntry(new_window, placeholder_text="Enter company name here", height=40)

    #why i chose focus out instead of key release
    fname.bind("<FocusOut>", lambda event: valid_name(fname, lbl1, valid_first))
    lname.bind("<FocusOut>", lambda event: valid_name(lname, lbl2, valid_last))
    email.bind("<FocusOut>", lambda event: valid_email())
    phone.bind("<FocusOut>", lambda event: valid_number())
    username.bind("<FocusOut>", lambda event: valid_username())
    company_name.bind("<FocusOut>", lambda event: save_comp())

    def update_check_button():
        if all([
            valid_first.get(),
            valid_last.get(),
            valid_email_var.get(),
            valid_phone.get(),
            valid_user.get(),
            valid_pass.get(),
            valid_company.get()
        ]):
            check.configure(state="normal", fg_color="green")
        else:
            check.configure(state="disabled", fg_color="gray")

    def open_msg(word):
        if word == "email":
            errormsg = ctk.CTkToplevel(new_window)
            errormsg.title("Unsuccessful")

            error_lbl = ctk.CTkLabel(errormsg, text="Email is already in use!")
            error_lbl.pack()

        elif word == "username":
            errormsg = ctk.CTkToplevel(new_window)
            errormsg.title("Unsuccessful")

            error_lbl = ctk.CTkLabel(errormsg, text="Username is already in use!")
            error_lbl.pack()

        else:
            errormsg = ctk.CTkToplevel(new_window)
            errormsg.title("Success")

            error_lbl = ctk.CTkLabel(errormsg, text="New member added successfully!")
            error_lbl.pack()


    def accept_new_user():
        new_member["name"] = {
            "first": fname.get().capitalize(),
            "last": lname.get().capitalize()
        }

        new_member["email"] = email.get()

        area = area_dropdown.get()
        new_member["phone"] = f"{area} {phone.get().strip()}"

        new_member["username"] = username.get()
        new_member["password"] = password.get()

        if check_trader.get() == "on":
            new_member["company"] = company_name.get()

        if any(member.get("email") == new_member["email"] for member in members):
            open_msg("email")
            
        elif any(member.get("username") == new_member["username"] for member in members):
            open_msg("username")
            
        else:
            members.append(new_member.copy())
            open_msg("success")

            print(members)
    


    check = ctk.CTkButton(new_window, text="Check", height=40, state="disabled", fg_color="gray", command=accept_new_user)
    check.grid(row=(new_row + 4), column=1, columnspan=2, sticky="ew", padx=10, pady=10)


btn = ctk.CTkButton(root, text="add_account", command=on_click)
btn.pack()

root.mainloop()