import customtkinter as ctk

members = {
    "name": {
        "first": "Sarah",
        "last": "Shaw"
    },
    "email": "123@gmail.com",
    "phone": "+64 0278293321",
    "username": "sarahs123",
    "password": "123!@#QWE"
}

root = ctk.CTk()

def open_signin():
    signin = ctk.CTkToplevel(root)
    signin.title("SIGN IN")
    signin.geometry("320x200")
    
    signin.columnconfigure(1, weight=1)
    signin.columnconfigure(2, weight=1)

    def check_user():
        if username.get() == members["username"] and password.get() == members["password"]:
            errormsg = ctk.CTkToplevel(signin)
            errormsg.title("Success")

            error_lbl = ctk.CTkLabel(errormsg, text="New member added successfully!")
            error_lbl.pack()

        else:
            errormsg = ctk.CTkToplevel(signin)
            errormsg.title("Unsuccessful")

            error_lbl = ctk.CTkLabel(errormsg, text="Incorrect password or username")
            error_lbl.pack()
    
    def filled_in(event):
        if password.get() and username.get():
            check.configure(state="normal", fg_color="green")
            lbl5.configure(text="Username", text_color="gray")
            lbl6.configure(text="Password", text_color="gray")
        else:
            check.configure(state="disabled", fg_color="gray")
            if not username.get():
                lbl5.configure(text="USERNAME REQUIRED", text_color="red")
            if not password.get():
                lbl6.configure(text="PASSWORD REQUIRED", text_color="red")


    lbl5 = ctk.CTkLabel(signin, text="Username", anchor="w")
    lbl5.grid(row=0, column=1, sticky="w", padx=10)

    username = ctk.CTkEntry(signin, placeholder_text="Username", height=40)
    username.grid(row=1, column=1, columnspan=2, sticky="ew", padx=10)
    username.bind("<KeyRelease>", filled_in)

    lbl6 = ctk.CTkLabel(signin, text="Password", anchor="w")
    lbl6.grid(row=2, column=1, sticky="w", padx=10)

    password = ctk.CTkEntry(signin, placeholder_text="Password", height=40)
    password.grid(row=3, column=1, columnspan=2, sticky="ew", padx=10)
    password.bind("<KeyRelease>", filled_in)
        
    check = ctk.CTkButton(signin, text="Check", height=40, state="disabled", fg_color="gray", command=check_user)
    check.grid(row=4, column=1, columnspan=2, sticky="ew", padx=10, pady=10)



btn = ctk.CTkButton(root, text="Sign In", command=open_signin)
btn.pack()


root.mainloop()