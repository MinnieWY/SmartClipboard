import tkinter as tk
from tkinter import ttk

class Notification(tk.Frame):
    # Define allowed colors as class-level constants
    ALLOWED_COLORS = {
        "success": "green",
        "error": "red",
        "warning": "orange",
        "info": "blue",
        "": "black"  # Default color
    }

    def __init__(self, parent):
        super().__init__(parent)
        self.label = ttk.Label(self, text="", foreground="green")
        self.label.pack(pady=5)
        self.pack()

    def show(self, message, color=""):
        # Validate the color input
        if color not in self.ALLOWED_COLORS:
            color = "green"  # Default to green if invalid color is provided

        self.label.config(text=message, foreground=self.ALLOWED_COLORS[color])
        self.after(3000, self.clear)  # Clear after 3 seconds

    def clear(self):
        self.label.config(text="")