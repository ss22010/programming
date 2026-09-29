import customtkinter as ctk

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

class SigninWindow(ctk.CTkToplevel):
    def __init__(self, root, members):
        super().__init__(root)

        self.members = members

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
            errormsg = ctk.CTkToplevel(self)
            errormsg.title("Success")

            error_lbl = ctk.CTkLabel(errormsg, text=f"Welcome back {self.username.get()}")
            error_lbl.pack()

        else:
            errormsg = ctk.CTkToplevel(self)
            errormsg.title("Unsuccessful")

            error_lbl = ctk.CTkLabel(errormsg, text="Incorrect password or username")
            error_lbl.pack()
    
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

    

def open_signin():
    SigninWindow(root, members)

btn = ctk.CTkButton(root, text="Sign In", command=open_signin)
btn.pack()


root.mainloop()