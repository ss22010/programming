import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Dashed Line Example")

        # 1. Create a frame
        self.frame = ctk.CTkFrame(self, fg_color="transparent")
        self.frame.pack(fill="x", padx=20, pady=20)

        # 2. Add a label above the line
        self.label1 = ctk.CTkLabel(self.frame, text="Item Above Line", font=("Arial", 16))
        self.label1.pack(pady=5)

        # 3. Create a canvas for the dashed line
        # Set highlightthickness=0 to remove the default canvas border
        self.line_canvas = ctk.CTkCanvas(
            self.frame, 
            height=2, 
            bg=self.frame.cget("fg_color"), 
            highlightthickness=0
        )
        self.line_canvas.pack(fill="x", pady=10)

        # 4. Bind the configure event to dynamically redraw the line on resize
        self.line_canvas.bind("<Configure>", self.draw_dashed_line)

        # 5. Add a label below the line
        self.label2 = ctk.CTkLabel(self.frame, text="Item Below Line", font=("Arial", 16))
        self.label2.pack(pady=5)

    def draw_dashed_line(self, event):
        # Clear previous line to prevent stacking memory leaks
        self.line_canvas.delete("all")
        
        # Get the current dynamic width of the canvas
        canvas_width = event.width
        
        # Draw the line from (0,0) to (width, 0)
        # 'dash' takes a tuple: (length of dash, length of space)
        self.line_canvas.create_line(
            0, 1, canvas_width, 1, 
            dash=(4, 4), 
            fill="gray", 
            width=1
        )

if __name__ == "__main__":
    app = App()
    app.mainloop()
