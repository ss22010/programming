import customtkinter as ctk

# Initialize the main window
app = ctk.CTk()
app.title("Phone Number Input")
app.geometry("450x150")

# Create a container frame to hold both widgets together
phone_frame = ctk.CTkFrame(app, fg_color="transparent")
phone_frame.pack(pady=40, padx=20)

# 1. Dropdown options combining country name and area code
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

# Area Code Dropdown (ComboBox)
area_code_dropdown = ctk.CTkComboBox(
    master=phone_frame,
    values=country_codes,
    width=180,         # Widened to comfortably fit country names
    state="readonly"   # Prevents users from typing custom text
)
area_code_dropdown.set("New Zealand (+64)") # Set default value
area_code_dropdown.grid(row=0, column=0, padx=(0, 5))

# 2. Phone Number Entry
phone_entry = ctk.CTkEntry(
    master=phone_frame,
    placeholder_text="Enter phone number",
    width=200
)
phone_entry.grid(row=0, column=1, padx=(5, 0))

# Function to extract only the area code and combine it with the input number
def get_full_number():
    selected_text = area_code_dropdown.get()
    
    # Extract code from between the parentheses: "United States (+1)" -> "+1"
    try:
        area_code = selected_text.split("(")[1].replace(")", "")
    except IndexError:
        area_code = "" # Fallback safety
        
    phone_digits = phone_entry.get().strip()
    
    full_number = f"{area_code} {phone_digits}"
    print(f"Cleaned Number: {full_number}")

# Submit Button
submit_btn = ctk.CTkButton(app, text="Submit", command=get_full_number)
submit_btn.pack(pady=10)

app.mainloop()
