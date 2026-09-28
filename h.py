import customtkinter as ctk

app = ctk.CTk()
app.geometry("300x200")

# 1. Create the checkbox in a disabled state so the user cannot click it
system_checkbox = ctk.CTkCheckBox(app, text="System Controlled Only", state="disabled")
system_checkbox.pack(pady=20)

# 2. Use a function to change the state via system logic
def toggle_checkbox_by_system():
    # Check current state using the variable or checking check status
    # Note: disabled widgets can still be modified by program methods
    if system_checkbox.get() == 0:
        system_checkbox.select()    # Ticks the box
    else:
        system_checkbox.deselect()  # Unticks the box

# Button to simulate a system or background event triggering the change
trigger_button = ctk.CTkButton(app, text="Simulate System Event", command=toggle_checkbox_by_system)
trigger_button.pack(pady=20)

app.mainloop()
