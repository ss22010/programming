import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x300")

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# 1. Create a widget with default scrollbars disabled
textbox = ctk.CTkTextbox(app, activate_scrollbars=False)
textbox.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=10)

# 2. Create the standalone CTkScrollbar
scrollbar = ctk.CTkScrollbar(app, command=textbox.yview)
scrollbar.grid(row=0, column=1, sticky="ns", padx=(0, 10), pady=10)

# 3. Link the textbox scrolling state back to the scrollbar
textbox.configure(yscrollcommand=scrollbar.set)

# Populate text to test scrolling
for i in range(50):
    textbox.insert("end", f"This is line {i + 1}\n")

app.mainloop()
