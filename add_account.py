import customtkinter as ctk
from tkinter import *
import re

root = ctk.CTk()

def on_click():
    new_window = ctk.CTkToplevel(master=root)
    new_window.title("add_acc_win")
    new_window.geometry("300x200")

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

    def valid_email():
        email_match = email.get()
        #talk about finding this and what it does
        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

        #also talk about re.fullmatch()
        if re.fullmatch(email_pattern, email_match):
            lbl3.configure(text="VALID EMAIL")
            print("yes")
        else:
            lbl3.configure(text="INVALID EMAIL")
            print("no")

    check_email = ctk.CTkButton(new_window, text="check", command=valid_email)
    check_email.grid(row=3, column=1)



btn = ctk.CTkButton(root, text="add_account", command=on_click)
btn.pack()

root.mainloop()