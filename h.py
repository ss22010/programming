import customtkinter as ctk

app = ctk.CTk()
app.geometry("300x200")


def on_checkbox_toggle():
  # Check the state of the variable
  if check_var.get() == 1:
    # Change to your desired color when checked
    checkbox.configure(fg_color="green")
  else:
    # Change back or set to the disabled/unchecked color
    checkbox.configure(fg_color="gray")


# Create a StringVar or IntVar to track the value
check_var = ctk.IntVar(value=1)  # Set to 1 if pre-ticked, 0 if not

checkbox = ctk.CTkCheckBox(
    master=app,
    text="Disabled Checkbox",
    state="disabled",
    text_color="white",  # Color when normal
    text_color_disabled="gray",  # Color when state="disabled"
)
checkbox.pack(padx=20, pady=20)


btn = ctk.CTkButton(app, command=on_checkbox_toggle)
btn.pack()
# Optional: You can still call select() or toggle() programmatically
# check_var.set(1) # updates state and triggers colors if handled

app.mainloop()
