import customtkinter as ctk
from PIL import Image

# Initialize the main window
app = ctk.CTk()
app.geometry("400x400")

# Load and create the CTkImage (supports separate light/dark modes)
my_image = ctk.CTkImage(
    light_image=Image.open("path/to/image.png"),
    dark_image=Image.open("path/to/image.png"),
    size=(150, 150)  # Width and height in pixels
)

# Display the image using a CTkLabel (set text="" to hide default text)
image_label = ctk.CTkLabel(app, image=my_image, text="")
image_label.pack(pady=20)

app.mainloop()

