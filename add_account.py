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

class SignupWindow(ctk.CTkToplevel):
    def __init__(self, root, members):
        super().__init__(root)

        self.members = members
        self.new_member = {}

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
        email_match = self.email.get()
        #talk about finding this and what it does
        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

        #also talk about re.fullmatch()
        if re.fullmatch(email_pattern, email_match):
            self.lbl3.configure(text="Email", text_color="gray")
            self.valid_email_var.set(True)
        elif any(member.get("email") == email_match for member in members):
            self.lbl3.configure(text="EMAIL ALREADY IN USE", text_color="red")
            self.valid_email_var.set(False)
        else:
            self.lbl3.configure(text="INVALID EMAIL", text_color="red")
            self.valid_email_var.set(False)
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


    def valid_email(self):
        email_match = self.email.get()
        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

        if not re.fullmatch(email_pattern, email_match):
            self.lbl3.configure(text="INVALID EMAIL", text_color="red")
            self.valid_email_var.set(False)

        elif any(member.get("email") == email_match for member in members):
            self.lbl3.configure(text="EMAIL ALREADY IN USE", text_color="red")
            self.valid_email_var.set(False)

        else:
            self.lbl3.configure(text="Email", text_color="gray")
            self.valid_email_var.set(True)

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


    def open_msg(self):
            errormsg = ctk.CTkToplevel(self)
            errormsg.title("Success")

            error_lbl = ctk.CTkLabel(errormsg, text="New member added successfully!")
            error_lbl.pack()


    def accept_new_user(self):
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
        self.open_msg("success")

        print(members)



def on_click():
    SignupWindow(root, members)

btn = ctk.CTkButton(root, text="add_account", command=on_click)
btn.pack()

root.mainloop()