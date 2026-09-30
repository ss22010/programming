
import customtkinter as ctk


root = ctk.CTk()
# Create a canvas that spans the full width and use its grid/pack configuration
canvas = ctk.CTkCanvas(
    master=root, 
    height=2, 
    bg="system_background_color_here", # Match your frame's background
    highlightthickness=0
)
canvas.pack(fill="x", pady=10)

# Bind the configure event to dynamically redraw the line when the frame resizes
def draw_line(event):
    canvas.delete("all")
    # Get the dynamic width from the event object
    width = event.width
    canvas.create_line(0, 1, width, 1, dash=(4, 4), fill="gray")

canvas.bind("<Configure>", draw_line)

root.mainloop()
